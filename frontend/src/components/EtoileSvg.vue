<template>
  <svg :width="taille" :height="taille" viewBox="0 0 100 100" aria-hidden="true">
    <path
      d="M50 5 L61 38 L98 38 L68 59 L79 92 L50 71 L21 92 L32 59 L2 38 L39 38 Z"
      fill="#fbbf24"
      stroke="#f59e0b"
      stroke-width="4"
      stroke-linejoin="round"
    />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 16 } })
</script>
