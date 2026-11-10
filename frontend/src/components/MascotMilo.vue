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
    <path d="M75 55 C86 50 91 39 88 30" stroke="#8b5cf6" stroke-width="9" stroke-linecap="round" />
    <g stroke="#8b5cf6" stroke-width="5" stroke-linecap="round">
      <path d="M85 29 L83 20" />
      <path d="M89 28 L91 19" />
      <path d="M86 31 L93 26" />
    </g>
    <!-- Petit bras gauche -->
    <path d="M24 66 C17 70 15 77 19 82" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round" />

    <!-- Corps dodu -->
    <ellipse cx="50" cy="61" rx="31" ry="33" fill="#8b5cf6" />

    <!-- Oreilles arrondies -->
    <ellipse cx="33" cy="26" rx="7" ry="10" transform="rotate(-18 33 26)" fill="#7c3aed" />
    <ellipse cx="67" cy="26" rx="7" ry="10" transform="rotate(18 67 26)" fill="#7c3aed" />

    <!-- Grands yeux brillants -->
    <ellipse cx="38" cy="48" rx="8.5" ry="9.5" fill="#ffffff" />
    <ellipse cx="62" cy="48" rx="8.5" ry="9.5" fill="#ffffff" />
    <circle cx="40" cy="51" r="4.2" fill="#2e1065" />
    <circle cx="60" cy="51" r="4.2" fill="#2e1065" />
    <circle cx="38.6" cy="49.4" r="1.4" fill="#ffffff" />
    <circle cx="58.6" cy="49.4" r="1.4" fill="#ffffff" />

    <!-- Joues roses -->
    <circle cx="29" cy="62" r="5" fill="#c4b5fd" opacity="0.75" />
    <circle cx="71" cy="62" r="5" fill="#c4b5fd" opacity="0.75" />

    <!-- Bouche ouverte souriante avec langue -->
    <path d="M42 65 Q50 77 58 65 Q50 69 42 65 Z" fill="#2e1065" />
    <ellipse cx="50" cy="70.5" rx="3.6" ry="2" fill="#fb7185" />

    <!-- Pieds -->
    <ellipse cx="38" cy="94" rx="8.5" ry="5" fill="#6d28d9" />
    <ellipse cx="62" cy="94" rx="8.5" ry="5" fill="#6d28d9" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 96 } })
</script>
