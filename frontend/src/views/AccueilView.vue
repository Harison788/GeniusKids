<template>
  <section class="accueil-nouveau">
    <!-- Bannière de bienvenue -->
    <div class="banniere">
      <span class="avatar-banniere">{{ apparence.avatar }}</span>
      <div class="textes-banniere">
        <h1 class="titre-banniere">Bonjour {{ progression.pseudo }} !</h1>
        <p class="question-banniere">Prêt à t'amuser ?</p>
        <p class="phrase-banniere">Apprendre en s'amusant, à ton rythme.</p>
      </div>
      <div class="carte-etoiles-banniere">
        <p class="ligne-etoiles-banniere"><span class="etoile-grand">⭐</span> {{ progression.etoiles }} étoiles</p>
        <p class="encouragement">Bravo, {{ progression.pseudo }} !</p>
      </div>
    </div>

    <div class="bloc-jeux">
      <div class="colonne-principale">
        <!-- "À toi de jouer !" : titres + filtres -->
        <div class="entete-jeux">
          <div>
            <h2 class="titre-section">À toi de jouer !</h2>
            <p class="sous-section">Un petit jeu, de grandes découvertes.</p>
          </div>
        </div>
        <div class="grille-filtres">
          <button
            v-for="f in filtres"
            :key="f"
            class="filtre"
            :class="{ 'est-actif': filtreActif === f }"
            @click="filtreActif = f"
          >
            {{ f }}
          </button>
        </div>

        <!-- Grille des jeux filtrée -->
        <div id="jeux" class="grille-jeux-nouvelle">
          <RouterLink
            v-for="jeu in jeuxAffiches"
            :key="jeu.chemin"
            :to="jeu.chemin"
            class="carte-jeu-nouvelle"
            :style="{ '--fond-carte': jeu.fond }"
          >
            <span class="icone-carte-jeu">{{ jeu.emoji }}</span>
            <span class="titre-jeu-carte">{{ jeu.titre }}</span>
            <span class="description-jeu">{{ jeu.description }}</span>
            <span class="record-jeu" v-if="meilleure(jeu.jeu)">
              Record : {{ meilleure(jeu.jeu).points }} pts
            </span>
            <span class="bouton-jouer">Jouer</span>
          </RouterLink>
        </div>
        <p v-if="jeuxAffiches.length === 0" class="vide-filtre">Aucun jeu dans cette catégorie pour l'instant.</p>
      </div>

      <!-- "Mon coin à moi" : l'espace personnel -->
      <aside class="mon-coin">
        <h2 class="titre-coin">Mon coin à moi</h2>

        <div class="carte-coin">
          <span class="avatar-coin">{{ apparence.avatar }}</span>
          <div class="textes-coin">
            <p class="nom-coin">{{ apparence.avatarNom }}</p>
            <p class="apres-coin">C'est toi !</p>
          </div>
        </div>

        <div class="boutons-coin">
          <button class="bouton-personnaliser" @click="ouvrirModal('profil')">
            Personnaliser mon animal
          </button>
          <button class="bouton-theme-coin" @click="ouvrirModal('themes')">
            {{ themeActuel().emoji }} Changer le thème
          </button>
        </div>

        <div class="carte-mon-niveau">
          <p class="titre-dans-carte">Mon niveau</p>
          <div class="choix-niveaux-coin">
            <button
              v-for="n in niveaux"
              :key="n.valeur"
              class="pastille-niveau"
              :class="{ 'est-choisie': progression.niveau === n.valeur }"
              @click="choisirNiveau(n.valeur)"
            >
              <span>{{ n.emoji }}</span>{{ n.nom }}
            </button>
          </div>
        </div>

        <div class="carte-bulle-mascotte">
          <div class="bulle-mascotte">
            <p class="titre-bulle-mascotte">Coucou, moi c'est Milo !</p>
            <p class="texte-bulle-mascotte">Choisis un jeu et amuse-toi !</p>
          </div>
          <span class="mascotte-coin">🦄</span>
          <p class="devise-mascotte">À chaque jeu, une découverte !</p>
        </div>
      </aside>
    </div>

    <ModalApparence v-if="modalOuverte" :onglet-initial="ongletModal" @fermer="modalOuverte = false" />
  </section>
</template>

<script setup>
import { computed, ref } from 'vue'
import { RouterLink } from 'vue-router'
import ModalApparence from '../components/ModalApparence.vue'
import {
  progression,
  meilleure,
  choisirNiveau,
} from '../stores/progression'
import { apparence, themeActuel } from '../stores/apparence'

const niveaux = [
  { valeur: 1, emoji: '🐿️', nom: 'Écureuil', ages: '4-6 ans' },
  { valeur: 2, emoji: '🦊', nom: 'Renard', ages: '6-8 ans' },
  { valeur: 3, emoji: '🦉', nom: 'Hibou', ages: '9-11 ans' },
]

const jeux = [
  { chemin: '/quiz', jeu: 'quiz', emoji: '➕', titre: 'Quiz de Maths', description: 'Joue avec les nombres', fond: '#ece5fd', categorie: 'nombres' },
  { chemin: '/comptage', jeu: 'comptage', emoji: '🔢', titre: 'Comptage', description: 'Compte avec nous', fond: '#fdf3d7', categorie: 'nombres' },
  { chemin: '/kakuro', jeu: 'kakuro', emoji: '➗', titre: 'Kakuro', description: 'À toi de calculer !', fond: '#ece5fd', categorie: 'nombres' },
  { chemin: '/memory', jeu: 'memory', emoji: '🃏', titre: 'Memory', description: 'Trouve les paires', fond: '#e8e4fb', categorie: 'memoire' },
  { chemin: '/associations', jeu: 'associations', emoji: '🔗', titre: 'Associations', description: 'Relie ce qui va ensemble', fond: '#e8e4fb', categorie: 'memoire' },
  { chemin: '/fruits', jeu: 'fruits', emoji: '🍓', titre: 'Fusion des fruits', description: "Fais le plein de fruits !", fond: '#fdeedd', categorie: 'creativite' },
  { chemin: '/puzzle', jeu: 'puzzle', emoji: '🧩', titre: 'Puzzles', description: 'Assemble et découvre', fond: '#dff2e9', categorie: 'creativite' },
  { chemin: '/points', jeu: 'points', emoji: '✏️', titre: 'Relie les Points', description: 'Dessine le dessin secret', fond: '#dff2e9', categorie: 'creativite' },
]

const filtres = ['Tous les jeux', 'Nombres', 'Mémoire', 'Créativité']
const filtreActif = ref('Tous les jeux')
const modalOuverte = ref(false)
const ongletModal = ref('profil')

function ouvrirModal(onglet) {
  ongletModal.value = onglet
  modalOuverte.value = true
}

const jeuxAffiches = computed(() => {
  if (filtreActif.value === 'Tous les jeux') return jeux
  const cles = { Nombres: 'nombres', Mémoire: 'memoire', Créativité: 'creativite' }
  return jeux.filter((jeu) => jeu.categorie === cles[filtreActif.value])
})
</script>
