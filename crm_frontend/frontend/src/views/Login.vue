<script setup>
import { ref } from 'vue'
import api from '../api'

const username = ref('')
const password = ref('')
const error = ref('')

const login = async () => {
  error.value = ''
  try {
    const { data } = await api.post('/token/', { username: username.value, password: password.value })
    localStorage.setItem('token', data.access)
    window.location.href = '/'
  } catch (e) {
    error.value = 'Invalid credentials'
  }
}
</script>

<template>
  <div class="max-w-md mx-auto">
    <div class="bg-white shadow-sm border rounded-lg p-6">
      <h3 class="text-lg font-semibold mb-4">Login</h3>

      <label class="block text-sm mb-1">Username</label>
      <input v-model="username" placeholder="Username"
        class="w-full border rounded-md px-3 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

      <label class="block text-sm mb-1">Password</label>
      <input v-model="password" type="password" placeholder="Password"
        class="w-full border rounded-md px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-200" />

      <button @click="login"
        class="w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-md px-4 py-2">
        Sign in
      </button>

      <p v-if="error" class="text-red-600 text-sm mt-3">{{ error }}</p>
    </div>
  </div>
</template>