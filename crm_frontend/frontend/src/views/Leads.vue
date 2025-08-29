<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'
import Notes from '../components/Notes.vue'
import Reminders from '../components/Reminders.vue'

const leads = ref([])
const form = ref({ id: null, name: '', status: 'new' })
const selectedLead = ref(null)
const statuses = ['new', 'contacted', 'qualified', 'lost']
const loading = ref(false)
const error = ref('')

const load = async () => {
  loading.value = true
  error.value = ''
  try {
    const { data } = await api.get('/leads/')
    leads.value = data
  } catch (e) {
    error.value = 'Failed to load leads. Are you logged in?'
  } finally {
    loading.value = false
  }
}

const resetForm = () => { form.value = { id: null, name: '', status: 'new' } }

const save = async () => {
  try {
    if (!form.value.name) return
    if (form.value.id) {
      await api.put(`/leads/${form.value.id}/`, { name: form.value.name, status: form.value.status })
    } else {
      await api.post('/leads/', { name: form.value.name, status: form.value.status })
    }
    resetForm()
    await load()
  } catch (e) {
    error.value = 'Save failed (check auth/fields).'
  }
}

const editLead = (l) => { form.value = { id: l.id, name: l.name, status: l.status } }

const del = async (id) => {
  if (!confirm('Delete lead?')) return
  try {
    await api.delete(`/leads/${id}/`)
    await load()
  } catch (e) {
    error.value = 'Delete failed (manager-only).'
  }
}

const selectLead = (lead) => {
  selectedLead.value = lead
}

onMounted(load)
</script>

<template>
  <div class="grid lg:grid-cols-3 gap-6">
    <div class="lg:col-span-1">
      <div class="bg-white border rounded-lg p-4 shadow-sm">
        <h3 class="text-base font-semibold mb-4">{{ form.id ? 'Edit lead' : 'Create lead' }}</h3>

        <label class="block text-sm mb-1">Name</label>
        <input v-model="form.name" placeholder="Lead name"
               class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

        <label class="block text-sm mb-1">Status</label>
        <select v-model="form.status"
                class="w-full border rounded-md px-3 py-2 mb-4 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-200">
          <option v-for="s in statuses" :key="s" :value="s">{{ s }}</option>
        </select>

        <div class="flex gap-2">
          <button @click="save"
                  class="bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-4 py-2">
            {{ form.id ? 'Update' : 'Create' }}
          </button>
          <button v-if="form.id" @click="resetForm"
                  class="border border-gray-300 hover:bg-gray-50 rounded-md px-4 py-2">
            Cancel
          </button>
        </div>

        <p v-if="error" class="text-red-600 text-sm mt-3">{{ error }}</p>
      </div>

      <!-- Notes section -->
      <div v-if="selectedLead" class="mt-6">
        <Notes :lead-id="selectedLead.id" />
      </div>

      <!-- Reminders section -->
      <div v-if="selectedLead" class="mt-6">
        <Reminders :lead-id="selectedLead.id" />
      </div>
    </div>

    <div class="lg:col-span-2">
      <div class="bg-white border rounded-lg p-4 shadow-sm">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-base font-semibold">Leads</h3>
          <span v-if="loading" class="text-sm text-gray-500">Loading…</span>
        </div>

        <div v-if="!leads.length" class="text-gray-500 text-sm">No leads yet.</div>

        <div v-else class="overflow-x-auto">
          <table class="min-w-full text-sm">
            <thead>
              <tr class="text-left text-gray-600">
                <th class="py-2">ID</th>
                <th class="py-2">Name</th>
                <th class="py-2">Status</th>
                <th class="py-2">Owner</th>
                <th class="py-2">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="l in leads" :key="l.id" class="border-t hover:bg-gray-50">
                <td class="py-2">{{ l.id }}</td>
                <td class="py-2 font-medium cursor-pointer" @click="selectLead(l)">{{ l.name }}</td>
                <td class="py-2">
                  <span
                    :class="{
                      'px-2 py-0.5 rounded-full text-xs font-medium': true,
                      'bg-gray-100 text-gray-700': l.status === 'new',
                      'bg-blue-100 text-blue-700': l.status === 'contacted',
                      'bg-green-100 text-green-700': l.status === 'qualified',
                      'bg-red-100 text-red-700': l.status === 'lost',
                    }"
                  >
                    {{ l.status }}
                  </span>
                </td>
                <td class="py-2">{{ l.owner ?? '-' }}</td>
                <td class="py-2">
                  <button @click="editLead(l)" class="text-indigo-700 hover:underline mr-3">Edit</button>
                  <button @click="del(l.id)" class="text-red-700 hover:underline">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </div>
  </div>
</template>
