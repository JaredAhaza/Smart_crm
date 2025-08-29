<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '../api'

const props = defineProps({
	contactId: { type: [String, Number], required: true }
})

const correspondences = ref([])
const newCorrespondence = ref({ type: 'call', subject: '', body: '', timestamp: '' })
const loading = ref(false)
const error = ref('')
const types = ['email', 'call', 'meeting']

const loadCorrespondences = async () => {
	if (!props.contactId) return
	loading.value = true
	error.value = ''
	try {
		const { data } = await api.get('/correspondence/', { params: { contact: props.contactId } })
		correspondences.value = data
	} catch (e) {
		error.value = 'Failed to load correspondence.'
	} finally {
		loading.value = false
	}
}

const addCorrespondence = async () => {
	if (!newCorrespondence.value.type || !newCorrespondence.value.timestamp) return
	try {
		await api.post('/correspondence/', {
			contact: props.contactId,
			type: newCorrespondence.value.type,
			subject: newCorrespondence.value.subject,
			body: newCorrespondence.value.body,
			timestamp: newCorrespondence.value.timestamp
		})
		newCorrespondence.value = { type: 'call', subject: '', body: '', timestamp: '' }
		await loadCorrespondences()
	} catch (e) {
		error.value = 'Failed to add correspondence.'
	}
}

watch(() => props.contactId, loadCorrespondences)
onMounted(loadCorrespondences)
</script>

<template>
	<div class="bg-white border rounded-lg p-4 shadow-sm">
		<h4 class="text-sm font-semibold mb-3">Correspondence</h4>
		
		<div class="mb-3 space-y-2">
			<select v-model="newCorrespondence.type"
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200">
				<option v-for="t in types" :key="t" :value="t">{{ t }}</option>
			</select>
			<input v-model="newCorrespondence.subject" placeholder="Subject..."
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200" />
			<textarea v-model="newCorrespondence.body" placeholder="Details..."
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200"
				rows="2"></textarea>
			<input v-model="newCorrespondence.timestamp" type="datetime-local"
				class="w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200" />
			<button @click="addCorrespondence" 
				class="bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-3 py-1.5 text-sm">
				Add Correspondence
			</button>
		</div>

		<p v-if="error" class="text-red-600 text-sm mb-3">{{ error }}</p>
		<p v-if="loading" class="text-gray-500 text-sm">Loading correspondence...</p>

		<div v-if="!correspondences.length && !loading" class="text-gray-500 text-sm">No correspondence yet.</div>

		<div v-else class="space-y-2">
			<div v-for="corr in correspondences" :key="corr.id" 
				class="border rounded-md p-2">
				<div class="flex justify-between items-start">
					<div>
						<div class="flex items-center gap-2">
							<span class="px-2 py-0.5 bg-blue-100 text-blue-700 text-xs rounded-full">
								{{ corr.type }}
							</span>
							<span class="text-sm font-medium">{{ corr.subject || 'No subject' }}</span>
						</div>
						<p v-if="corr.body" class="text-sm mt-1">{{ corr.body }}</p>
						<p class="text-xs text-gray-500 mt-1">
							{{ new Date(corr.timestamp).toLocaleString() }}
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
