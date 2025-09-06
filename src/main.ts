import { createApp } from 'vue'
import Root from './Root.vue'
import router from './router'

// global reset to neutralize outside styles
import './assets/reset.css'

createApp(Root).use(router).mount('#app')

