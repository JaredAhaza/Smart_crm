<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '../api'

const props = defineProps({
	leadId: { type: [String, Number], required: true }
})

const reminders = ref([])
const newReminder = ref({ description: '', remind_at: '' })
const loading = ref(false)
const error = ref('')

const loadReminders = async () => {
	if (!props.leadId) return
	loading.value = true
	error.value = ''
	try {
		const { data } = await api.get('/reminders/', { params: { lead: props.leadId } })
		reminders.value = data
	} catch (e) {
		error.value = 'Failed to load reminders.'
	} finally {
		loading.value = false
	}
}

const addReminder = async () => {
	if (!newReminder.value.description || !newReminder.value.remind_at) return
	try {
		await api.post('/reminders/', {
			lead: props.leadId,
			description: newReminder.value.description,
			remind_at: newReminder.value.remind_at
		})
		newReminder.value = { description: '', remind_at: '' }
		await loadReminders()
	} catch (e) {
		error.value = 'Failed to add reminder.'
	}
}

const deleteReminder = async (id) => {
	if (!confirm('Delete reminder?')) return
	try {
		await api.delete(`/reminders/${id}/`)
		await loadReminders()
	} catch (e) {
		error.value = 'Failed to delete reminder.'
	}
}

watch(() => props.leadId, loadReminders)
onMounted(loadReminders)
</script>

<template>
	<div class="bg-white border rounded-lg p-4 shadow-sm">
		<h4 class="text-sm font-semibold mb-3">Reminders</h4>
		
		<div class="mb-3 space-y-2">
			<input v-model="newReminder.description" placeholder="Reminder description..."
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200" />
			<input v-model="newReminder.remind_at" type="datetime-local"
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200" />
			<button @click="addReminder" 
				class="bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-3 py-1.5 text-sm">
				Add Reminder
			</button>
		</div>

		<p v-if="error" class="text-red-600 text-sm mb-3">{{ error }}</p>
		<p v-if="loading" class="text-gray-500 text-sm">Loading reminders...</p>

		<div v-if="!reminders.length && !loading" class="text-gray-500 text-sm">No reminders yet.</div>

		<div v-else class="space-y-2">
			<div v-for="reminder in reminders" :key="reminder.id" 
				class="border rounded-md p-2">
				<div class="flex justify-between items-start">
					<div>
						<p class="text-sm font-medium">{{ reminder.description }}</p>
						<p class="text-xs text-gray-500">
							{{ new Date(reminder.remind_at).toLocaleString() }}
						</p>
						<span v-if="reminder.is_sent" 
							class="inline-block px-2 py-0.5 bg-green-100 text-green-700 text-xs rounded-full mt-1">
							Sent
						</span>
					</div>
					<button @click="deleteReminder(reminder.id)" 
						class="text-red-600 hover:text-red-800 text-xs">
						Delete
					</button>
				</div>
			</div>
		</div>
	</div>
</template>