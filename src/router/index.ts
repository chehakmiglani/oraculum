import { createRouter, createWebHistory } from 'vue-router'

// Static imports for stability (dynamic imports were intermittently failing in dev HMR)
import LoginPage from '../components/LoginPage.vue'
import App from '../App.vue'
import ChatView from '../views/tools/ChatView.vue'
import ResumeAnalyzerView from '../views/tools/ResumeAnalyzerView.vue'
import RoadmapView from '../views/tools/RoadmapView.vue'
import CoverLetterView from '../views/tools/CoverLetterView.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginPage,
    },
    { path: '/tools/chat', name: 'chat', component: ChatView },
    { path: '/tools/resume', name: 'resume', component: ResumeAnalyzerView },
    { path: '/tools/roadmap', name: 'roadmap', component: RoadmapView },
    { path: '/tools/cover-letter', name: 'cover-letter', component: CoverLetterView },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: App,
    },
    { path: '/about', name: 'about', component: AboutView },
  ],
})

export default router
