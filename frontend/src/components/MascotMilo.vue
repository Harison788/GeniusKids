<template>
  <svg
    :width="taille"
    :height="taille"
    viewBox="0 0 100 100"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
    class="overflow-visible"
  >
    <!-- Bras levé qui salue (3 petits doigts) -->
    <path d="M74 52 C85 47 90 36 87 27" stroke="#8b5cf6" stroke-width="10" stroke-linecap="round" />
    <g stroke="#8b5cf6" stroke-width="5.5" stroke-linecap="round">
      <path d="M84 26 L81 17" />
      <path d="M88 25 L91 17" />
      <path d="M85 28 L93 23" />
    </g>
    <!-- Petit bras gauche baissé -->
    <path d="M22 68 C15 73 14 80 19 84" stroke="#8b5cf6" stroke-width="9" stroke-linecap="round" />

    <!-- Corps bien rond -->
    <ellipse cx="50" cy="59" rx="30" ry="32" fill="#8b5cf6" />

    <!-- Ventre clair -->
    <ellipse cx="50" cy="70" rx="20" ry="17" fill="#ece2ff" />

    <!-- Oreilles -->
    <ellipse cx="32" cy="26" rx="6.5" ry="9" transform="rotate(-16 32 26)" fill="#7c3aed" />
    <ellipse cx="68" cy="26" rx="6.5" ry="9" transform="rotate(16 68 26)" fill="#7c3aed" />

    <!-- Grands yeux sombres brillants (comme le prototype) -->
    <ellipse cx="38.5" cy="47" rx="6.8" ry="8.2" fill="#3b2a6b" />
    <ellipse cx="61.5" cy="47" rx="6.8" ry="8.2" fill="#3b2a6b" />
    <circle cx="36.4" cy="44.4" r="2.2" fill="#ffffff" />
    <circle cx="59.4" cy="44.4" r="2.2" fill="#ffffff" />
    <circle cx="40.5" cy="49.5" r="1" fill="#b7a6f5" opacity="0.9" />
    <circle cx="63.5" cy="49.5" r="1" fill="#b7a6f5" opacity="0.9" />

    <!-- Joues roses bien visibles -->
    <circle cx="27" cy="60" r="5.5" fill="#f7a8d8" />
    <circle cx="73" cy="60" r="5.5" fill="#f7a8d8" />

    <!-- Grande bouche ouverte souriante -->
    <path d="M41 60 Q50 78 59 60 Q50 65 41 60 Z" fill="#3b2a6b" />
    <path d="M45 65.5 Q50 73.5 55 65.5 Q50 68.5 45 65.5 Z" fill="#e15f94" />

    <!-- Pieds -->
    <ellipse cx="38" cy="92" rx="8.5" ry="5" fill="#7c3aed" />
    <ellipse cx="62" cy="92" rx="8.5" ry="5" fill="#7c3aed" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 96 } })
</script>
