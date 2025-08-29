<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '../api'

const props = defineProps({
	leadId: { type: [String, Number], required: true }
})

const notes = ref([])
const newNote = ref('')
const loading = ref(false)
const error = ref('')

const loadNotes = async () => {
	if (!props.leadId) return
	loading.value = true
	error.value = ''
	try {
		const { data } = await api.get('/notes/', { params: { lead: props.leadId } })
		notes.value = data
	} catch (e) {
		error.value = 'Failed to load notes.'
	} finally {
		loading.value = false
	}
}

const addNote = async () => {
	if (!newNote.value.trim()) return
	try {
		await api.post('/notes/', { lead: props.leadId, content: newNote.value })
		newNote.value = ''
		await loadNotes()
	} catch (e) {
		error.value = 'Failed to add note.'
	}
}

watch(() => props.leadId, loadNotes)
onMounted(loadNotes)
</script>

<template>
	<div class="bg-white border rounded-lg p-4 shadow-sm">
		<h4 class="text-sm font-semibold mb-3">Notes</h4>
		
		<div class="mb-3">
			<textarea v-model="newNote" placeholder="Add a note..."
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200"
				rows="2"></textarea>
			<button @click="addNote" 
				class="mt-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-3 py-1.5 text-sm">
				Add Note
			</button>
		</div>

		<p v-if="error" class="text-red-600 text-sm mb-3">{{ error }}</p>
		<p v-if="loading" class="text-gray-500 text-sm">Loading notes...</p>

		<div v-if="!notes.length && !loading" class="text-gray-500 text-sm">No notes yet.</div>

		<div v-else class="space-y-2">
			<div v-for="note in notes" :key="note.id" class="border-l-2 border-indigo-200 pl-3 py-1">
				<p class="text-sm">{{ note.content }}</p>
				<p class="text-xs text-gray-500 mt-1">
					{{ new Date(note.created_at).toLocaleString() }}
				</p>
			</div>
		</div>
	</div>
</template>
