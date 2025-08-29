import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import Leads from './views/Leads.vue'
import Contacts from './views/Contacts.vue'
import Audit from './views/Audit.vue'

const routes = [
	{ path: '/login', name: 'login', component: Login },
	{ path: '/register', name: 'register', component: Register },
	{ path: '/', name: 'leads', component: Leads },
	{ path: '/contacts', name: 'contacts', component: Contacts },
	{ path: '/audit', name: 'audit', component: Audit },
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
