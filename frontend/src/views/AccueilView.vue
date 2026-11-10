<template>
  <div class="flex flex-col gap-6">
    <WelcomeBanner />

    <div class="grid grid-cols-1 items-start gap-6 lg:grid-cols-[minmax(0,1fr)_265px]">
      <GameSection />
      <UserSidebar @personnaliser="ouvrirModal" />
    </div>

    <ModalApparence
      v-if="modalOuverte"
      :onglet-initial="ongletModal"
      @fermer="modalOuverte = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import WelcomeBanner from '../components/WelcomeBanner.vue'
import GameSection from '../components/GameSection.vue'
import UserSidebar from '../components/UserSidebar.vue'
import ModalApparence from '../components/ModalApparence.vue'

const modalOuverte = ref(false)
const ongletModal = ref('profil')

function ouvrirModal(onglet) {
  ongletModal.value = onglet
  modalOuverte.value = true
}
</script>
