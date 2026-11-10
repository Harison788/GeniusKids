<template>
  <header class="sticky top-0 z-30 border-b-2 border-indigo-600 bg-white">
    <div class="mx-auto flex max-w-6xl items-center gap-4 px-4 py-3 sm:px-6">
      <!-- Logo -->
      <RouterLink to="/" class="flex items-center gap-2.5">
        <span class="grid h-10 w-10 place-items-center rounded-xl bg-purple-100">
          <MascotMilo :taille="30" />
        </span>
        <span class="text-lg font-extrabold text-purple-700">les petits curieux</span>
      </RouterLink>

      <!-- Navigation centrale -->
      <nav class="mx-auto flex items-center gap-1">
        <RouterLink
          to="/"
          class="flex items-center gap-1.5 rounded-full px-4 py-2 text-sm font-bold transition-colors"
          exact-active-class="bg-purple-100 text-purple-700"
          :class="$route.path === '/' ? '' : 'text-slate-600 hover:bg-slate-100'"
        >
          <IconeMaison /> Accueil
        </RouterLink>
        <a
          href="/#jeux"
          class="flex items-center gap-1.5 rounded-full px-4 py-2 text-sm font-bold text-slate-600 transition-colors hover:bg-slate-100"
          @click.prevent="allerAuxJeux"
        >
          <IconeManette /> Jeux
        </a>
        <RouterLink
          to="/recompenses"
          class="flex items-center gap-1.5 rounded-full px-4 py-2 text-sm font-bold transition-colors"
          active-class="bg-purple-100 text-purple-700"
          :class="$route.path === '/recompenses' ? '' : 'text-slate-600 hover:bg-slate-100'"
        >
          <IconeTrophee /> Récompenses
        </RouterLink>
      </nav>

      <!-- Étoiles + profil -->
      <div class="ml-auto flex items-center gap-3 sm:ml-0">
        <RouterLink
          to="/recompenses"
          class="flex items-center gap-1.5 rounded-full border-2 border-amber-300 bg-amber-50 px-4 py-1.5 text-sm font-extrabold text-amber-700"
          title="Tes étoiles"
        >
          <EtoileSvg :taille="18" /> {{ progression.etoiles }}
        </RouterLink>

        <div class="relative">
          <button
            class="flex items-center gap-2 rounded-full py-1.5 pl-1.5 pr-3 text-sm font-bold text-slate-700 transition-colors hover:bg-purple-50"
            @click="menuOuvert = !menuOuvert"
          >
            <span class="grid h-9 w-9 place-items-center rounded-full bg-purple-100 text-xl leading-none">
              {{ apparence.avatar }}
            </span>
            Mon profil
            <svg width="10" height="10" viewBox="0 0 10 10" class="text-slate-400" fill="none">
              <path d="M2 3.5 L5 6.5 L8 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </button>

          <div
            v-if="menuOuvert"
            class="absolute right-0 top-12 w-60 rounded-2xl border border-purple-100 bg-white p-2 shadow-xl shadow-purple-100"
          >
            <button
              v-for="option in options"
              :key="option.label"
              class="flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-left text-sm font-bold text-slate-700 transition-colors hover:bg-purple-50"
              @click="option.action()"
            >
              <span class="text-lg leading-none">{{ option.icone }}</span>
              {{ option.label }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <ModalApparence
      v-if="modalOuverte"
      :onglet-initial="ongletModal"
      @fermer="modalOuverte = false"
    />
  </header>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import MascotMilo from './MascotMilo.vue'
import ModalApparence from './ModalApparence.vue'
import IconeMaison from './IconeMaison.vue'
import IconeManette from './IconeManette.vue'
import IconeTrophee from './IconeTrophee.vue'
import EtoileSvg from './EtoileSvg.vue'
import { progression } from '../stores/progression'
import { apparence, themeActuel } from '../stores/apparence'

const route = useRoute()
const router = useRouter()
const menuOuvert = ref(false)
const modalOuverte = ref(false)
const ongletModal = ref('profil')

function ouvrirModal(onglet) {
  menuOuvert.value = false
  ongletModal.value = onglet
  modalOuverte.value = true
}

const options = computed(() => [
  { label: 'Changer mon avatar', icone: apparence.avatar, action: () => ouvrirModal('profil') },
  { label: 'Changer mon thème', icone: themeActuel().emoji, action: () => ouvrirModal('themes') },
])

function allerAuxJeux() {
  menuOuvert.value = false
  router.push('/')
  setTimeout(() => {
    document.getElementById('jeux')?.scrollIntoView({ behavior: 'smooth' })
  }, 150)
}

/* Ferme le menu déroulant quand on clique ailleurs. */
function clicExterieur(evenement) {
  if (!evenement.target.closest('.relative')) menuOuvert.value = false
}

/* Ferme le menu quand on change de page. */
watch(() => route.path, () => { menuOuvert.value = false })

onMounted(() => document.addEventListener('click', clicExterieur))
onBeforeUnmount(() => document.removeEventListener('click', clicExterieur))
</script>
