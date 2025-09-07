import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import NoteList from './components/NoteList.vue'
import NoteEditor from './components/NoteEditor.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/notes', component: NoteList },
  { path: '/notes/new', component: NoteEditor },
  { path: '/notes/:id/edit', component: NoteEditor, props: true }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
