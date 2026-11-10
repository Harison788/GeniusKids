import { createRouter, createWebHistory } from 'vue-router'
import AccueilView from './views/AccueilView.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'accueil', component: AccueilView },
    { path: '/recompenses', name: 'recompenses', component: () => import('./views/RecompensesView.vue') },
    { path: '/quiz', name: 'quiz', component: () => import('./views/QuizView.vue') },
    { path: '/comptage', name: 'comptage', component: () => import('./views/ComptageView.vue') },
    { path: '/memory', name: 'memory', component: () => import('./views/MemoryView.vue') },
    { path: '/associations', name: 'associations', component: () => import('./views/AssociationsView.vue') },
    { path: '/kakuro', name: 'kakuro', component: () => import('./views/KakuroView.vue') },
    { path: '/points', name: 'points', component: () => import('./views/PointsView.vue') },
    { path: '/fruits', name: 'fruits', component: () => import('./views/FruitsView.vue') },
    { path: '/puzzle', name: 'puzzle', component: () => import('./views/PuzzleView.vue') },
  ],
  scrollBehavior(to) {
    if (to.hash) {
      return new Promise((resoudre) => {
        setTimeout(() => {
          resoudre({ el: to.hash, behavior: 'smooth' })
        }, 120)
      })
    }
    return { top: 0 }
  },
})
