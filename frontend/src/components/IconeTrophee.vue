<template>
  <svg :width="taille" :height="taille" viewBox="0 0 24 24" fill="none" aria-hidden="true">
    <path
      d="M7 3.5 H17 V9.5 A5 5 0 0 1 7 9.5 Z M7 5.5 H3.5 A3.2 3.2 0 0 0 7 9.5 M17 5.5 H20.5 A3.2 3.2 0 0 1 17 9.5"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path d="M12 14.5 V17.5 M8.5 20.5 H15.5 M12 17.5 C12 19 10.5 20.5 8.5 20.5 M12 17.5 C12 19 13.5 20.5 15.5 20.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 15 } })
</script>
