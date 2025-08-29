<script setup>
import { ref } from 'vue'
import axios from 'axios'  // Import axios directly

const form = ref({ username: '', email: '', password: '', role: 'agent' })
const error = ref('')
const success = ref('')
const roles = ['manager', 'agent']

const register = async () => {
	error.value = ''
	success.value = ''
	
	try {
		// Use axios directly without the interceptor for registration
		const response = await axios.post('http://127.0.0.1:8000/api/register/', form.value)
		success.value = response.data.message
		form.value = { username: '', email: '', password: '', role: 'agent' }
	} catch (e) {
		console.error('Registration error:', e.response?.data || e.message)
		error.value = e.response?.data?.error || 'Registration failed'
	}
}
</script>

<template>
	<div class="max-w-md mx-auto">
		<div class="bg-white shadow-sm border rounded-lg p-6">
			<h3 class="text-lg font-semibold mb-4">Register New User</h3>

			<label class="block text-sm mb-1">Username</label>
			<input v-model="form.username" placeholder="Username"
				class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

			<label class="block text-sm mb-1">Email</label>
			<input v-model="form.email" type="email" placeholder="Email"
				class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

			<label class="block text-sm mb-1">Password</label>
			<input v-model="form.password" type="password" placeholder="Password"
				class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

			<label class="block text-sm mb-1">Role</label>
			<select v-model="form.role"
				class="w-full border rounded-md px-3 py-2 mb-4 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-200">
				<option v-for="role in roles" :key="role" :value="role">{{ role }}</option>
			</select>

			<button @click="register"
				class="w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-4 py-2">
				Register User
			</button>

			<p v-if="error" class="text-red-600 text-sm mt-3">{{ error }}</p>
			<p v-if="success" class="text-green-600 text-sm mt-3">{{ success }}</p>
		</div>
	</div>
</template>
