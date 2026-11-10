import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './styles.css'
import { enregistrerServiceWorker } from './pwa'

enregistrerServiceWorker()

createApp(App).use(router).mount('#app')
