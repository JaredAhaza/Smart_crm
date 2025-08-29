import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Leads from './views/Leads.vue'

const routes = [
	{ path: '/login', name: 'login', component: Login },
	{ path: '/', name: 'leads', component: Leads },
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
