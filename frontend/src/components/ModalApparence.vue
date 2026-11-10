<template>
  <div class="modal-fond" @click.self="$emit('fermer')">
    <div class="modal-carte" role="dialog" aria-label="Personnaliser ton profil">
      <button class="modal-fermer" @click="$emit('fermer')" aria-label="Fermer">✕</button>

      <div class="modal-onglets">
        <button
          class="onglet"
          :class="{ 'est-active': onglet === 'profil' }"
          @click="onglet = 'profil'"
        >
          Mon profil
        </button>
        <button
          class="onglet"
          :class="{ 'est-active': onglet === 'themes' }"
          @click="onglet = 'themes'"
        >
          Mes thèmes
        </button>
      </div>

      <!-- Onglet profil : prénom + avatar -->
      <div v-if="onglet === 'profil'" class="modal-section">
        <div class="modal-apercu">
          <span class="apercu-avatar">{{ apparence.avatar }}</span>
          <div class="apercu-textes">
            <input
              class="champ-pseudo-modal"
              :value="pseudoLocal"
              maxlength="20"
              aria-label="Ton prénom"
              @change="changerPseudo"
            />
            <p class="apercu-nom">{{ apparence.avatarNom }}</p>
          </div>
        </div>

        <div v-for="groupe in AVATARS" :key="groupe.groupe" class="groupe-avatar">
          <p class="titre-groupe">{{ groupe.groupe }}</p>
          <div class="liste-avatars">
            <button
              v-for="avatar in groupe.liste"
              :key="avatar.emoji"
              class="tuile-avatar"
              :class="{ 'est-choisie': apparence.avatar === avatar.emoji }"
              :title="avatar.nom"
              @click="choisirAvatar(avatar)"
            >
              {{ avatar.emoji }}
            </button>
          </div>
        </div>
      </div>

      <!-- Onglet thèmes : le décor du jeu -->
      <div v-else class="modal-section">
        <p class="note-theme">
          Le thème change les couleurs et le décor derrière les jeux.
          Le violet doux est celui de départ.
        </p>
        <div class="liste-themes">
          <button
            v-for="theme in THEMES"
            :key="theme.id"
            class="carte-theme"
            :class="{ 'est-choisie': apparence.theme === theme.id }"
            @click="choisirTheme(theme.id)"
          >
            <span class="apercu-theme" :style="{ background: theme.apercu }">{{ theme.emoji }}</span>
            <span class="nom-theme">{{ theme.nom }}</span>
            <span class="coche-theme" v-if="apparence.theme === theme.id">Choisi ✓</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { apparence, AVATARS, THEMES, choisirAvatar, choisirTheme } from '../stores/apparence'
import { progression, choisirPseudo, enregistrer } from '../stores/progression'

const props = defineProps({ ongletInitial: { type: String, default: 'profil' } })
defineEmits(['fermer'])

const onglet = ref(props.ongletInitial)
const pseudoLocal = ref(progression.pseudo)

function changerPseudo(evenement) {
  choisirPseudo(evenement.target.value)
  evenement.target.value = progression.pseudo
  pseudoLocal.value = progression.pseudo
  enregistrer()
}
</script>
