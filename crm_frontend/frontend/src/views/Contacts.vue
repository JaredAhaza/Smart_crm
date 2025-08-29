<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '../api'
import Correspondence from '../components/Correspondence.vue'

const leads = ref([])
const contacts = ref([])
const form = ref({ id: null, first_name: '', last_name: '', email: '', phone: '', lead: '' })
const filterLead = ref('')
const loading = ref(false)
const error = ref('')
const selectedContact = ref(null)

const loadLeads = async () => {
	try {
		const { data } = await api.get('/leads/')
		leads.value = data
	} catch (e) {
		// ignore
	}
}

const loadContacts = async () => {
	loading.value = true
	error.value = ''
	try {
		const params = filterLead.value ? { lead: filterLead.value } : {}
		const { data } = await api.get('/contacts/', { params })
		contacts.value = data
	} catch (e) {
		error.value = 'Failed to load contacts.'
	} finally {
		loading.value = false
	}
}

const resetForm = () => { form.value = { id: null, first_name: '', last_name: '', email: '', phone: '', lead: '' } }

const save = async () => {
	try {
		const payload = {
			first_name: form.value.first_name,
			last_name: form.value.last_name,
			email: form.value.email,
			phone: form.value.phone,
			lead: form.value.lead,
		}
		if (!payload.first_name || !payload.last_name || !payload.lead) return
		if (form.value.id) await api.put(`/contacts/${form.value.id}/`, payload)
		else await api.post('/contacts/', payload)
		resetForm()
		await loadContacts()
	} catch (e) {
		error.value = 'Save failed.'
	}
}

const editItem = (c) => {
	form.value = {
		id: c.id,
		first_name: c.first_name,
		last_name: c.last_name,
		email: c.email,
		phone: c.phone,
		lead: c.lead,
	}
}

const del = async (id) => {
	if (!confirm('Delete contact?')) return
	try {
		await api.delete(`/contacts/${id}/`)
		await loadContacts()
	} catch (e) {
		error.value = 'Delete failed (manager-only).'
	}
}

const selectContact = (contact) => {
	selectedContact.value = contact
}

watch(filterLead, loadContacts)

onMounted(async () => {
	await loadLeads()
	await loadContacts()
})
</script>

<template>
  <div class="grid lg:grid-cols-3 gap-6">
    <div class="lg:col-span-1">
      <div class="bg-white border rounded-lg p-4 shadow-sm">
        <h3 class="text-base font-semibold mb-4">{{ form.id ? 'Edit contact' : 'Create contact' }}</h3>

        <label class="block text-sm mb-1">Lead</label>
        <select v-model="form.lead"
                class="w-full border rounded-md px-3 py-2 mb-3 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-200">
          <option disabled value="">Select a lead</option>
          <option v-for="l in leads" :key="l.id" :value="l.id">{{ l.name }}</option>
        </select>

        <label class="block text-sm mb-1">First name</label>
        <input v-model="form.first_name"
               class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

        <label class="block text-sm mb-1">Last name</label>
        <input v-model="form.last_name"
               class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

        <label class="block text-sm mb-1">Email</label>
        <input v-model="form.email" type="email"
               class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

        <label class="block text-sm mb-1">Phone</label>
        <input v-model="form.phone"
               class="w-full border rounded-md px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

        <div class="flex gap-2">
          <button @click="save" class="bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-4 py-2">
            {{ form.id ? 'Update' : 'Create' }}
          </button>
          <button v-if="form.id" @click="resetForm" class="border border-gray-300 hover:bg-gray-50 rounded-md px-4 py-2">
            Cancel
          </button>
        </div>

        <p v-if="error" class="text-red-600 text-sm mt-3">{{ error }}</p>
      </div>

      <!-- Correspondence section -->
      <div v-if="selectedContact" class="mt-6">
        <Correspondence :contact-id="selectedContact.id" />
      </div>
    </div>

    <div class="lg:col-span-2">
      <div class="bg-white border rounded-lg p-4 shadow-sm">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-base font-semibold">Contacts</h3>
          <div class="flex items-center gap-2">
            <select v-model="filterLead"
                    class="border rounded-md px-3 py-1.5 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-200">
              <option value="">All leads</option>
              <option v-for="l in leads" :key="l.id" :value="l.id">{{ l.name }}</option>
            </select>
            <span v-if="loading" class="text-sm text-gray-500">Loading…</span>
          </div>
        </div>

        <div v-if="!contacts.length" class="text-gray-500 text-sm">No contacts yet.</div>

        <div v-else class="overflow-x-auto">
          <table class="min-w-full text-sm">
            <thead>
              <tr class="text-left text-gray-600">
                <th class="py-2">ID</th>
                <th class="py-2">Name</th>
                <th class="py-2">Email</th>
                <th class="py-2">Phone</th>
                <th class="py-2">Lead</th>
                <th class="py-2">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in contacts" :key="c.id" class="border-t">
                <td class="py-2">{{ c.id }}</td>
                <td class="py-2 font-medium cursor-pointer" @click="selectContact(c)">
                  {{ c.first_name }} {{ c.last_name }}
                </td>
                <td class="py-2">{{ c.email || '-' }}</td>
                <td class="py-2">{{ c.phone || '-' }}</td>
                <td class="py-2">
                  <span class="px-2 py-0.5 rounded-full text-xs bg-gray-100 text-gray-700">{{ c.lead }}</span>
                </td>
                <td class="py-2">
                  <button @click="editItem(c)" class="text-indigo-700 hover:underline mr-3">Edit</button>
                  <button @click="del(c.id)" class="text-red-700 hover:underline">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </div>
  </div>
</template>
