import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Leads from './views/Leads.vue'
import Contacts from './views/Contacts.vue'

const routes = [
	{ path: '/login', name: 'login', component: Login },
	{ path: '/', name: 'leads', component: Leads },
	{ path: '/contacts', name: 'contacts', component: Contacts },
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
