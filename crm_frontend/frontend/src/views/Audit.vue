<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const auditLogs = ref([])
const loading = ref(false)
const error = ref('')

const loadAuditLogs = async () => {
	loading.value = true
	error.value = ''
	try {
		const { data } = await api.get('/audit/')
		auditLogs.value = data
	} catch (e) {
		error.value = 'Failed to load audit logs.'
	} finally {
		loading.value = false
	}
}

onMounted(loadAuditLogs)
</script>

<template>
	<div class="bg-white border rounded-lg p-4 shadow-sm">
		<h3 class="text-base font-semibold mb-4">Audit Trail</h3>
		
		<p v-if="error" class="text-red-600 text-sm mb-3">{{ error }}</p>
		<p v-if="loading" class="text-gray-500 text-sm">Loading audit logs...</p>

		<div v-if="!auditLogs.length && !loading" class="text-gray-500 text-sm">No audit logs yet.</div>

		<div v-else class="space-y-3">
			<div v-for="log in auditLogs" :key="log.id" class="border rounded-md p-3">
				<div class="flex justify-between items-start">
					<div>
						<div class="flex items-center gap-2">
							<span class="px-2 py-0.5 rounded-full text-xs font-medium"
								:class="{
									'bg-green-100 text-green-700': log.action === 'created',
									'bg-blue-100 text-blue-700': log.action === 'updated',
									'bg-red-100 text-red-700': log.action === 'deleted'
								}">
								{{ log.action }}
							</span>
							<span class="text-sm font-medium">{{ log.content_type_name }}</span>
							<span class="text-sm text-gray-500">ID: {{ log.object_id }}</span>
						</div>
						<p class="text-xs text-gray-500 mt-1">
							By: {{ log.user_name || 'Unknown' }} | {{ new Date(log.created_at).toLocaleString() }}
						</p>
						<div v-if="Object.keys(log.changes).length" class="mt-2 text-xs">
							<div v-for="(change, field) in log.changes" :key="field" class="mb-1">
								<strong>{{ field }}:</strong> 
								<span class="text-gray-600">{{ change.from }} → {{ change.to }}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
