<template>
  <div class="appli">
    <header class="entete">
      <RouterLink to="/" class="logo">
        <span class="logo-rond">🧮</span>
        <span class="logo-texte">GeniusKids</span>
      </RouterLink>

      <nav class="menu">
        <RouterLink to="/" class="lien-menu" exact-active-class="est-lieu">
          <span class="icone-menu">🏠</span> Accueil
        </RouterLink>
        <a href="/#jeux" class="lien-menu" @click="allerAuxJeux">
          <span class="icone-menu">🎮</span> Jeux
        </a>
        <RouterLink to="/recompenses" class="lien-menu" active-class="est-lieu">
          <span class="icone-menu">🏆</span> Récompenses
        </RouterLink>
      </nav>

      <div class="zone-profil">
        <RouterLink to="/recompenses" class="badge-etoiles" title="Tes étoiles">
          <span class="etoile-badge">⭐</span> {{ progression.etoiles }}
        </RouterLink>

        <div class="menu-profil">
          <button class="bouton-profil" @click="$event => menuOuvert = !menuOuvert">
            <span class="avatar-mini">{{ apparence.avatar }}</span>
            Mon profil
            <span class="fleche-profil">▾</span>
          </button>

          <div v-if="menuOuvert" class="panneau-profil">
            <button class="option-profil" @click="ouvrirModal('profil')">
              <span class="option-emoji">{{ apparence.avatar }}</span>
              Changer mon avatar
            </button>
            <button class="option-profil" @click="ouvrirModal('themes')">
              <span class="option-emoji">{{ themeActuel().emoji }}</span>
              Changer mon thème
            </button>
          </div>
        </div>
      </div>
    </header>

    <main class="contenu">
      <RouterView />
    </main>

    <footer class="pied">
      <div class="pied-marque">
        <span class="logo-texte">GeniusKids</span>
        <span class="pied-devise">Grandir, un jeu à la fois.</span>
      </div>
      <div class="pied-liens">
        <span class="lien-pied" title="Un espace pour les parents arrive bientôt">Espace parents</span>
        <span class="lien-pied" title="De l'aide arrive bientôt">Aide</span>
      </div>
    </footer>

    <ModalApparence
      v-if="modalOuverte"
      :onglet-initial="ongletModal"
      @fermer="modalOuverte = false"
    />
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import ModalApparence from './components/ModalApparence.vue'
import { progression } from './stores/progression'
import { apparence, themeActuel } from './stores/apparence'

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

function allerAuxJeux(evenement) {
  evenement.preventDefault()
  menuOuvert.value = false
  router.push('/')
  setTimeout(() => {
    document.getElementById('jeux')?.scrollIntoView({ behavior: 'smooth' })
  }, 150)
}

/* Le thème se lit dans <body data-theme="..."> pour colorer tout le fond. */
function appliquerTheme() {
  document.body.dataset.theme = apparence.theme
}

/* Ferme le menu déroulant quand on clique ailleurs. */
function fermerMenu(evenement) {
  if (!evenement.target.closest('.menu-profil')) menuOuvert.value = false
}

/* Ferme le menu quand on change de page. */
watch(() => route.path, () => { menuOuvert.value = false })

watch(() => apparence.theme, appliquerTheme)

onMounted(() => {
  appliquerTheme()
  document.addEventListener('click', fermerMenu)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', fermerMenu)
})
</script>
