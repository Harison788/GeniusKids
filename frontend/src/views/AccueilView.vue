<template>
  <section class="accueil">
    <div class="carte-accueil">
      <h1 class="titre-accueil">Salut {{ progression.pseudo }} !</h1>
      <div class="rangee-profil">
        <input
          class="champ-pseudo"
          :value="progression.pseudo"
          maxlength="20"
          @change="changerPseudo"
          aria-label="Ton prénom"
        />
        <div class="badge-etoiles grand">⭐ {{ progression.etoiles }} étoiles</div>
      </div>

      <h2 class="sous-titre">Choisis ton niveau</h2>
      <div class="grille-niveaux">
        <button
          v-for="niveau in niveaux"
          :key="niveau.valeur"
          class="carte-niveau"
          :class="{ 'est-active': progression.niveau === niveau.valeur }"
          @click="choisirNiveau(niveau.valeur)"
        >
          <span class="emoji-niveau">{{ niveau.emoji }}</span>
          <span class="nom-niveau">{{ niveau.nom }}</span>
          <span class="age-niveau">{{ niveau.ages }}</span>
        </button>
      </div>
    </div>

    <!-- Univers 1 : Apprendre -->
    <div class="entete-univers apprendre">
      <span class="badge-univers">Apprendre</span>
      <p class="sous-titre-univers">Les jeux qui font travailler le cerveau</p>
    </div>
    <div class="grille-jeux">
      <RouterLink
        v-for="jeu in jeuxApprendre"
        :key="jeu.chemin"
        :to="jeu.chemin"
        class="carte-jeu"
        :style="{ '--couleur': jeu.couleur }"
      >
        <span class="emoji-jeu">{{ jeu.emoji }}</span>
        <span class="titre-jeu-carte">{{ jeu.titre }}</span>
        <span class="description-jeu">{{ jeu.description }}</span>
        <span class="record-jeu" v-if="meilleure(jeu.jeu)">
          Record : {{ meilleure(jeu.jeu).points }} pts
        </span>
        <span class="record-jeu" v-else>Joue pour la première fois !</span>
      </RouterLink>
    </div>

    <!-- Univers 2 : S'amuser -->
    <div class="entete-univers plaisir">
      <span class="badge-univers">S'amuser</span>
      <p class="sous-titre-univers">Les jeux juste pour le plaisir</p>
    </div>
    <div class="grille-jeux">
      <RouterLink
        v-for="jeu in jeuxPlaisir"
        :key="jeu.chemin"
        :to="jeu.chemin"
        class="carte-jeu"
        :style="{ '--couleur': jeu.couleur }"
      >
        <span class="emoji-jeu">{{ jeu.emoji }}</span>
        <span class="titre-jeu-carte">{{ jeu.titre }}</span>
        <span class="description-jeu">{{ jeu.description }}</span>
        <span class="record-jeu" v-if="meilleure(jeu.jeu)">
          Record : {{ meilleure(jeu.jeu).points }} pts
        </span>
        <span class="record-jeu" v-else>Joue pour la première fois !</span>
      </RouterLink>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import {
  progression,
  meilleure,
  choisirPseudo,
  choisirNiveau,
  enregistrer,
} from '../stores/progression'

const niveaux = [
  { valeur: 1, emoji: '🐿️', nom: 'Écureuil', ages: '4-6 ans' },
  { valeur: 2, emoji: '🦊', nom: 'Renard', ages: '6-8 ans' },
  { valeur: 3, emoji: '🦉', nom: 'Hibou', ages: '9-11 ans' },
]

const jeux = [
  { chemin: '/quiz', jeu: 'quiz', emoji: '➕', titre: 'Quiz de Maths', description: 'Additions, soustractions, multiplications', couleur: '#219ebc', categorie: 'apprendre' },
  { chemin: '/comptage', jeu: 'comptage', emoji: '🔢', titre: 'Comptage', description: 'Compte les objets et complète les suites', couleur: '#ffb703', categorie: 'apprendre' },
  { chemin: '/memory', jeu: 'memory', emoji: '🃏', titre: 'Memory', description: 'Retourne les cartes et trouve les paires', couleur: '#fb8500', categorie: 'apprendre' },
  { chemin: '/associations', jeu: 'associations', emoji: '🔗', titre: 'Associations', description: 'Relie ce qui va avec quoi', couleur: '#8e44ad', categorie: 'apprendre' },
  { chemin: '/kakuro', jeu: 'kakuro', emoji: '🧊', titre: 'Kakuro', description: 'Chaque ligne et colonne fait la bonne somme', couleur: '#ef476f', categorie: 'apprendre' },
  { chemin: '/points', jeu: 'points', emoji: '✏️', titre: 'Relie les Points', description: 'Suis les numéros et dessine le dessin secret', couleur: '#14967f', categorie: 'plaisir' },
  { chemin: '/fruits', jeu: 'fruits', emoji: '🍓', titre: 'Fusion des Fruits', description: "Deux identiques deviennent un plus gros : 🍓+🍓→🍇, jusqu'à la 🍉", couleur: '#f3722c', categorie: 'plaisir' },
  { chemin: '/puzzle', jeu: 'puzzle', emoji: '🧩', titre: 'Puzzle', description: 'Échange les pièces pour recomposer le dessin', couleur: '#5a7d2a', categorie: 'plaisir' },
]

const jeuxApprendre = jeux.filter((jeu) => jeu.categorie === 'apprendre')
const jeuxPlaisir = jeux.filter((jeu) => jeu.categorie === 'plaisir')

function changerPseudo(evenement) {
  choisirPseudo(evenement.target.value)
  evenement.target.value = progression.pseudo
  enregistrer()
}
</script>
