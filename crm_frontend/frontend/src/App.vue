<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <header class="bg-white border-b">
      <div class="max-w-6xl mx-auto px-4 py-4 flex items-center gap-4">
        <h1 class="text-xl font-semibold tracking-tight">Smart CRM</h1>
        <nav class="flex items-center gap-3 ml-6">
          <router-link to="/" class="text-sm hover:text-indigo-600">Leads</router-link>
        </nav>
        <div class="ml-auto">
          <router-link to="/login" class="text-sm text-white bg-indigo-600 hover:bg-indigo-700 px-3 py-1.5 rounded-md">Login</router-link>
        </div>
      </div>
    </header>
    <main class="max-w-6xl mx-auto px-4 py-6">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
