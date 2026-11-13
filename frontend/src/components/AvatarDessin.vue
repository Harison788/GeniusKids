<template>
  <!-- Avatars dessinés (même style que Milo) ; repli sur l'emoji si inconnu. -->
  <svg
    :width="taille"
    :height="taille"
    viewBox="0 0 100 100"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
    class="shrink-0 overflow-visible"
  >
    <!-- 🦊 Renard -->
    <template v-if="emoji === '🦊'">
      <path d="M22 40 L26 12 L46 26 Z" fill="#e2622b" />
      <path d="M78 40 L74 12 L54 26 Z" fill="#e2622b" />
      <path d="M27 34 L29 20 L41 29 Z" fill="#f7b8a4" />
      <path d="M73 34 L71 20 L59 29 Z" fill="#f7b8a4" />
      <circle cx="50" cy="58" r="30" fill="#f0923f" />
      <ellipse cx="50" cy="70" rx="17" ry="12" fill="#fff3e3" />
      <ellipse cx="40" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="60" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="38.8" cy="50" r="1.4" fill="#ffffff" />
      <circle cx="58.8" cy="50" r="1.4" fill="#ffffff" />
      <circle cx="50" cy="66" r="4" fill="#4a2c1a" />
      <circle cx="29" cy="63" r="5" fill="#f7a8d8" />
      <circle cx="71" cy="63" r="5" fill="#f7a8d8" />
      <path d="M44 74 Q50 79 56 74" stroke="#4a2c1a" stroke-width="3" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🐱 Chat -->
    <template v-else-if="emoji === '🐱'">
      <path d="M24 42 L26 16 L44 26 Z" fill="#f2b04c" />
      <path d="M76 42 L74 16 L56 26 Z" fill="#f2b04c" />
      <path d="M29 36 L30 24 L40 31 Z" fill="#f7b8a4" />
      <path d="M71 36 L70 24 L60 31 Z" fill="#f7b8a4" />
      <circle cx="50" cy="58" r="29" fill="#f2b04c" />
      <path d="M16 60 L28 62 M14 68 L27 68 M84 60 L72 62 M86 68 L73 68" stroke="#c98a3a" stroke-width="2.5" stroke-linecap="round" />
      <ellipse cx="40" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="60" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="38.8" cy="50" r="1.4" fill="#ffffff" />
      <circle cx="58.8" cy="50" r="1.4" fill="#ffffff" />
      <path d="M46 64 L54 64 L50 69 Z" fill="#f77fa8" />
      <path d="M44 72 Q47 76 50 72 Q53 76 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <circle cx="28" cy="63" r="4.5" fill="#f7a8d8" />
      <circle cx="72" cy="63" r="4.5" fill="#f7a8d8" />
    </template>

    <!-- 🐶 Chien -->
    <template v-else-if="emoji === '🐶'">
      <ellipse cx="20" cy="52" rx="9" ry="17" transform="rotate(-12 20 52)" fill="#8d5a2b" />
      <ellipse cx="80" cy="52" rx="9" ry="17" transform="rotate(12 80 52)" fill="#8d5a2b" />
      <circle cx="50" cy="58" r="29" fill="#c98a4b" />
      <ellipse cx="50" cy="70" rx="16" ry="12" fill="#fff3e3" />
      <ellipse cx="40" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="60" cy="52" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="38.8" cy="50" r="1.4" fill="#ffffff" />
      <circle cx="58.8" cy="50" r="1.4" fill="#ffffff" />
      <ellipse cx="50" cy="66" rx="5" ry="4" fill="#3b2a6b" />
      <path d="M46 72 Q50 77 54 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <ellipse cx="50" cy="79" rx="5" ry="3.5" fill="#f77fa8" />
      <circle cx="28" cy="62" r="4.5" fill="#f7a8d8" />
      <circle cx="72" cy="62" r="4.5" fill="#f7a8d8" />
    </template>

    <!-- 🐼 Panda -->
    <template v-else-if="emoji === '🐼'">
      <circle cx="30" cy="28" r="10" fill="#33313f" />
      <circle cx="70" cy="28" r="10" fill="#33313f" />
      <circle cx="50" cy="58" r="30" fill="#ffffff" stroke="#e3ddf2" stroke-width="3" />
      <ellipse cx="38" cy="52" rx="8" ry="9" transform="rotate(-14 38 52)" fill="#33313f" />
      <ellipse cx="62" cy="52" rx="8" ry="9" transform="rotate(14 62 52)" fill="#33313f" />
      <circle cx="39" cy="51" r="3" fill="#ffffff" />
      <circle cx="61" cy="51" r="3" fill="#ffffff" />
      <circle cx="40.5" cy="53" r="1.2" fill="#8b8fa8" />
      <circle cx="62.5" cy="53" r="1.2" fill="#8b8fa8" />
      <ellipse cx="50" cy="66" rx="5" ry="4" fill="#33313f" />
      <path d="M44 72 Q50 78 56 72" stroke="#33313f" stroke-width="3" stroke-linecap="round" fill="none" />
      <circle cx="28" cy="65" r="4.5" fill="#f7a8d8" />
      <circle cx="72" cy="65" r="4.5" fill="#f7a8d8" />
    </template>

    <!-- 🐰 Lapin -->
    <template v-else-if="emoji === '🐰'">
      <ellipse cx="35" cy="22" rx="8" ry="20" fill="#fdfdfd" stroke="#e3ddf2" stroke-width="3" />
      <ellipse cx="65" cy="22" rx="8" ry="20" fill="#fdfdfd" stroke="#e3ddf2" stroke-width="3" />
      <ellipse cx="35" cy="22" rx="3.5" ry="13" fill="#f7b8c4" />
      <ellipse cx="65" cy="22" rx="3.5" ry="13" fill="#f7b8c4" />
      <circle cx="50" cy="60" r="28" fill="#fdfdfd" stroke="#e3ddf2" stroke-width="3" />
      <ellipse cx="40" cy="55" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="60" cy="55" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="38.8" cy="53" r="1.4" fill="#ffffff" />
      <circle cx="58.8" cy="53" r="1.4" fill="#ffffff" />
      <path d="M46 66 L54 66 L50 71 Z" fill="#f77fa8" />
      <rect x="45" y="73" width="4.5" height="7" rx="2" fill="#ffffff" stroke="#e3ddf2" stroke-width="1.5" />
      <rect x="50.5" y="73" width="4.5" height="7" rx="2" fill="#ffffff" stroke="#e3ddf2" stroke-width="1.5" />
      <circle cx="29" cy="66" r="4.5" fill="#f7a8d8" />
      <circle cx="71" cy="66" r="4.5" fill="#f7a8d8" />
    </template>

    <!-- 🦁 Lion -->
    <template v-else-if="emoji === '🦁'">
      <circle cx="50" cy="58" r="35" fill="#dd8a3f" />
      <path d="M50 20 L55 12 L60 20 L66 14 L68 22 L76 20 L72 28 L80 30 L72 34" stroke="#dd8a3f" stroke-width="5" stroke-linecap="round" fill="none" />
      <path d="M50 20 L45 12 L40 20 L34 14 L32 22 L24 20 L28 28 L20 30 L28 34" stroke="#dd8a3f" stroke-width="5" stroke-linecap="round" fill="none" />
      <circle cx="50" cy="58" r="25" fill="#f2b25a" />
      <circle cx="41" cy="53" r="3.6" fill="#3b2a6b" />
      <circle cx="59" cy="53" r="3.6" fill="#3b2a6b" />
      <circle cx="40" cy="51.6" r="1.2" fill="#ffffff" />
      <circle cx="58" cy="51.6" r="1.2" fill="#ffffff" />
      <ellipse cx="50" cy="68" rx="12" ry="9" fill="#ffe9c9" />
      <circle cx="50" cy="64" r="3.5" fill="#4a2c1a" />
      <path d="M45 70 Q50 74 55 70" stroke="#4a2c1a" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <circle cx="33" cy="64" r="4" fill="#f7a8d8" />
      <circle cx="67" cy="64" r="4" fill="#f7a8d8" />
    </template>

    <!-- 🐸 Grenouille -->
    <template v-else-if="emoji === '🐸'">
      <circle cx="36" cy="32" r="12" fill="#7cc45e" />
      <circle cx="64" cy="32" r="12" fill="#7cc45e" />
      <circle cx="36" cy="31" r="7" fill="#ffffff" />
      <circle cx="64" cy="31" r="7" fill="#ffffff" />
      <circle cx="37" cy="32.5" r="3.4" fill="#3b2a6b" />
      <circle cx="63" cy="32.5" r="3.4" fill="#3b2a6b" />
      <circle cx="36.2" cy="31" r="1.1" fill="#ffffff" />
      <circle cx="62.2" cy="31" r="1.1" fill="#ffffff" />
      <ellipse cx="50" cy="64" rx="29" ry="26" fill="#7cc45e" />
      <ellipse cx="50" cy="76" rx="18" ry="12" fill="#d8f0c8" />
      <circle cx="32" cy="62" r="5" fill="#9fd88a" />
      <circle cx="68" cy="62" r="5" fill="#9fd88a" />
      <path d="M38 62 Q50 74 62 62" stroke="#3b2a6b" stroke-width="3.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🦉 Hibou -->
    <template v-else-if="emoji === '🦉'">
      <path d="M26 32 L22 14 L38 24 Z" fill="#7a5138" />
      <path d="M74 32 L78 14 L62 24 Z" fill="#7a5138" />
      <circle cx="50" cy="56" r="30" fill="#9a6b4f" />
      <circle cx="38" cy="50" r="11" fill="#ffffff" stroke="#6d4a35" stroke-width="3" />
      <circle cx="62" cy="50" r="11" fill="#ffffff" stroke="#6d4a35" stroke-width="3" />
      <circle cx="38" cy="50" r="4.6" fill="#3b2a6b" />
      <circle cx="62" cy="50" r="4.6" fill="#3b2a6b" />
      <circle cx="36.5" cy="48" r="1.5" fill="#ffffff" />
      <circle cx="60.5" cy="48" r="1.5" fill="#ffffff" />
      <path d="M45 62 L55 62 L50 70 Z" fill="#f2a33c" />
      <path d="M32 76 Q40 82 50 80 Q60 82 68 76" stroke="#6d4a35" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <circle cx="28" cy="66" r="4" fill="#f7a8d8" />
      <circle cx="72" cy="66" r="4" fill="#f7a8d8" />
    </template>

    <!-- 🐙 Pieuvre -->
    <template v-else-if="emoji === '🐙'">
      <path d="M26 78 Q20 92 30 94 M42 80 Q38 94 46 96 M58 80 Q62 94 54 96 M74 78 Q80 92 70 94" stroke="#a78bfa" stroke-width="8" stroke-linecap="round" fill="none" />
      <circle cx="50" cy="52" r="30" fill="#a78bfa" />
      <ellipse cx="40" cy="48" rx="4.5" ry="6" fill="#3b2a6b" />
      <ellipse cx="60" cy="48" rx="4.5" ry="6" fill="#3b2a6b" />
      <circle cx="38.6" cy="46" r="1.5" fill="#ffffff" />
      <circle cx="58.6" cy="46" r="1.5" fill="#ffffff" />
      <circle cx="29" cy="60" r="5" fill="#c9b6ff" />
      <circle cx="71" cy="60" r="5" fill="#c9b6ff" />
      <path d="M43 60 Q50 68 57 60" stroke="#3b2a6b" stroke-width="3" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🦄 Licorne -->
    <template v-else-if="emoji === '🦄'">
      <circle cx="72" cy="46" r="10" fill="#a8d8f8" />
      <circle cx="76" cy="60" r="9" fill="#c9a8f8" />
      <circle cx="72" cy="73" r="8" fill="#f7a8d8" />
      <path d="M34 42 L26 30 L44 32 Z" fill="#f9d34c" />
      <path d="M31 37 L39 38 M33 31 L41 32" stroke="#e5a916" stroke-width="2" stroke-linecap="round" />
      <circle cx="50" cy="60" r="28" fill="#fdfdfd" stroke="#e3ddf2" stroke-width="3" />
      <path d="M30 46 Q34 30 50 28 Q62 28 66 38 L58 44 Q46 40 38 48 Z" fill="#f7a8d8" />
      <ellipse cx="42" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="60" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="40.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="58.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="28" cy="68" r="4.5" fill="#f7a8d8" />
      <circle cx="68" cy="68" r="4.5" fill="#f7a8d8" />
      <path d="M45 72 Q50 77 55 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🐢 Tortue -->
    <template v-else-if="emoji === '🐢'">
      <path d="M18 44 Q50 8 82 44" fill="#5f9e6c" />
      <path d="M28 38 Q50 18 72 38" stroke="#8fc98a" stroke-width="4" stroke-linecap="round" fill="none" />
      <circle cx="50" cy="62" r="26" fill="#8fc98a" />
      <ellipse cx="41" cy="56" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="56" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="54" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="54" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="66" r="4.5" fill="#c0e0b8" />
      <circle cx="70" cy="66" r="4.5" fill="#c0e0b8" />
      <path d="M44 70 Q50 76 56 70" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 👦 Garçon -->
    <template v-else-if="emoji === '👦'">
      <path d="M20 58 Q20 26 50 26 Q80 26 80 58 L74 58 Q74 40 50 38 Q26 40 26 58 Z" fill="#6b4630" />
      <circle cx="50" cy="60" r="26" fill="#f8c99a" />
      <path d="M24 56 Q26 40 50 38 Q74 40 76 56 L74 56 Q68 44 50 44 Q32 44 26 56 Z" fill="#6b4630" />
      <ellipse cx="41" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="70" r="4" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="4" fill="#f7a8d8" />
      <path d="M44 72 Q50 78 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 👧 Fille -->
    <template v-else-if="emoji === '👧'">
      <circle cx="24" cy="36" r="10" fill="#5f3a26" />
      <circle cx="76" cy="36" r="10" fill="#5f3a26" />
      <circle cx="24" cy="33" r="4" fill="#f77fa8" />
      <circle cx="76" cy="33" r="4" fill="#f77fa8" />
      <circle cx="50" cy="60" r="26" fill="#f8c99a" />
      <path d="M24 56 Q26 38 50 36 Q74 38 76 56 L76 62 Q70 44 50 44 Q30 44 24 62 Z" fill="#5f3a26" />
      <ellipse cx="41" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="70" r="4" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="4" fill="#f7a8d8" />
      <path d="M44 72 Q50 78 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🧑‍🚀 Astronaute -->
    <template v-else-if="emoji === '🧑‍🚀'">
      <line x1="50" y1="26" x2="50" y2="18" stroke="#c9c2e8" stroke-width="4" stroke-linecap="round" />
      <circle cx="50" cy="15" r="5" fill="#f77fa8" />
      <circle cx="50" cy="56" r="34" fill="#f4f2fb" stroke="#c9c2e8" stroke-width="4" />
      <rect x="28" y="40" width="44" height="34" rx="17" fill="#3b2a6b" />
      <ellipse cx="41" cy="56" rx="4" ry="5" fill="#ffffff" />
      <ellipse cx="59" cy="56" rx="4" ry="5" fill="#ffffff" />
      <circle cx="39.8" cy="54" r="1.4" fill="#ffffff" opacity="0" />
      <circle cx="39.8" cy="54" r="1.3" fill="#3b2a6b" />
      <circle cx="57.8" cy="54" r="1.3" fill="#3b2a6b" />
      <path d="M45 64 Q50 68 55 64" stroke="#8fd3ff" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <rect x="38" y="82" width="24" height="8" rx="4" fill="#c9c2e8" />
    </template>

    <!-- 🧚‍♀️ Fée -->
    <template v-else-if="emoji === '🧚‍♀️'">
      <ellipse cx="22" cy="52" rx="12" ry="20" transform="rotate(-28 22 52)" fill="#cfe8ff" opacity="0.9" />
      <ellipse cx="78" cy="52" rx="12" ry="20" transform="rotate(28 78 52)" fill="#cfe8ff" opacity="0.9" />
      <circle cx="50" cy="60" r="26" fill="#f8c99a" />
      <path d="M26 54 Q28 38 50 36 Q72 38 74 54 Q68 42 50 42 Q32 42 26 54 Z" fill="#f2c14e" />
      <path d="M44 34 L50 24 L56 34" stroke="#f2c14e" stroke-width="4" stroke-linecap="round" fill="none" />
      <path d="M47 26 L53 26 M50 23 L50 29" stroke="#f77fa8" stroke-width="2.5" stroke-linecap="round" />
      <ellipse cx="41" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="70" r="4" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="4" fill="#f7a8d8" />
      <path d="M44 72 Q50 78 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🦸‍♂️ Super héros -->
    <template v-else-if="emoji === '🦸‍♂️'">
      <circle cx="50" cy="58" r="28" fill="#f8c99a" />
      <path d="M24 56 Q26 40 50 38 Q74 40 76 56 L74 56 Q68 46 50 46 Q32 46 26 56 Z" fill="#3f3556" />
      <path d="M26 54 Q30 46 50 46 Q70 46 74 54 L74 60 Q70 52 50 52 Q30 52 26 60 Z" fill="#6d28d9" />
      <ellipse cx="40" cy="60" rx="4" ry="5" fill="#ffffff" />
      <ellipse cx="60" cy="60" rx="4" ry="5" fill="#ffffff" />
      <circle cx="40" cy="60.5" r="2" fill="#3b2a6b" />
      <circle cx="60" cy="60.5" r="2" fill="#3b2a6b" />
      <circle cx="28" cy="72" r="4" fill="#f7a8d8" />
      <circle cx="72" cy="72" r="4" fill="#f7a8d8" />
      <path d="M44 76 Q50 81 56 76" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <path d="M50 86 L52 92 L58 92 L53 95 L55 101 L50 97 L45 101 L47 95 L42 92 L48 92 Z" fill="#fbbf24" />
    </template>

    <!-- 🦸‍♀️ Super héroïne -->
    <template v-else-if="emoji === '🦸‍♀️'">
      <circle cx="50" cy="58" r="28" fill="#f8c99a" />
      <path d="M22 60 Q22 34 50 34 Q78 34 78 60 L78 70 Q70 48 50 48 Q30 48 22 70 Z" fill="#8d5a2b" />
      <path d="M26 54 Q30 46 50 46 Q70 46 74 54 L74 60 Q70 52 50 52 Q30 52 26 60 Z" fill="#db2777" />
      <ellipse cx="40" cy="60" rx="4" ry="5" fill="#ffffff" />
      <ellipse cx="60" cy="60" rx="4" ry="5" fill="#ffffff" />
      <circle cx="40" cy="60.5" r="2" fill="#3b2a6b" />
      <circle cx="60" cy="60.5" r="2" fill="#3b2a6b" />
      <circle cx="28" cy="72" r="4" fill="#f7a8d8" />
      <circle cx="72" cy="72" r="4" fill="#f7a8d8" />
      <path d="M44 76 Q50 81 56 76" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <path d="M50 86 L52 92 L58 92 L53 95 L55 101 L50 97 L45 101 L47 95 L42 92 L48 92 Z" fill="#fbbf24" />
    </template>

    <!-- 🤴 Prince -->
    <template v-else-if="emoji === '🤴'">
      <path d="M32 26 L36 12 L44 20 L50 8 L56 20 L64 12 L68 26 Z" fill="#f9d34c" stroke="#e5a916" stroke-width="2" />
      <circle cx="50" cy="60" r="27" fill="#f8c99a" />
      <path d="M25 58 Q27 42 50 40 Q73 42 75 58 Q68 46 50 46 Q32 46 25 58 Z" fill="#6b4630" />
      <ellipse cx="41" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="70" r="4" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="4" fill="#f7a8d8" />
      <path d="M44 72 Q50 78 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 👸 Princesse -->
    <template v-else-if="emoji === '👸'">
      <path d="M18 70 Q14 34 50 32 Q86 34 82 70 L82 82 Q74 60 50 58 Q26 60 18 82 Z" fill="#f2c14e" />
      <circle cx="50" cy="60" r="26" fill="#f8c99a" />
      <path d="M32 28 L37 18 L44 26 L50 16 L56 26 L63 18 L68 28 Z" fill="#f9d34c" stroke="#e5a916" stroke-width="2" />
      <circle cx="50" cy="23" r="3.5" fill="#f77fa8" />
      <path d="M25 54 Q27 42 50 40 Q73 42 75 54 Q68 46 50 46 Q32 46 25 54 Z" fill="#f2c14e" />
      <ellipse cx="41" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <ellipse cx="59" cy="60" rx="4" ry="5.5" fill="#3b2a6b" />
      <circle cx="39.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="57.8" cy="58" r="1.4" fill="#ffffff" />
      <circle cx="30" cy="70" r="4" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="4" fill="#f7a8d8" />
      <path d="M44 72 Q50 78 56 72" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🧙‍♂️ Magicien -->
    <template v-else-if="emoji === '🧙‍♂️'">
      <path d="M34 34 L58 6 L64 36 Z" fill="#6d28d9" />
      <ellipse cx="52" cy="37" rx="24" ry="6" fill="#7c3aed" />
      <path d="M55 16 L57 20 L61 20 L58 22 L59 26 L55 24 L51 26 L52 22 L49 20 L53 20 Z" fill="#fbbf24" />
      <circle cx="50" cy="62" r="26" fill="#f8c99a" />
      <path d="M28 70 Q34 88 50 88 Q66 88 72 70 Q64 78 50 78 Q36 78 28 70 Z" fill="#e8e4f4" />
      <path d="M28 58 Q30 46 50 44 Q70 46 72 58 Q62 50 50 50 Q38 50 28 58 Z" fill="#e8e4f4" />
      <ellipse cx="41" cy="62" rx="3.6" ry="5" fill="#3b2a6b" />
      <ellipse cx="59" cy="62" rx="3.6" ry="5" fill="#3b2a6b" />
      <circle cx="40" cy="60" r="1.2" fill="#ffffff" />
      <circle cx="58" cy="60" r="1.2" fill="#ffffff" />
      <circle cx="30" cy="70" r="3.5" fill="#f7a8d8" />
      <circle cx="70" cy="70" r="3.5" fill="#f7a8d8" />
      <circle cx="50" cy="74" r="2.5" fill="#c98a8a" />
    </template>

    <!-- 🥷 Ninja -->
    <template v-else-if="emoji === '🥷'">
      <circle cx="50" cy="58" r="30" fill="#3b3b4f" />
      <rect x="26" y="46" width="48" height="26" rx="13" fill="#f8c99a" />
      <path d="M22 44 Q50 32 78 44" stroke="#2b2b3b" stroke-width="10" stroke-linecap="round" fill="none" />
      <ellipse cx="40" cy="58" rx="4" ry="5" fill="#3b2a6b" />
      <ellipse cx="60" cy="58" rx="4" ry="5" fill="#3b2a6b" />
      <circle cx="38.8" cy="56" r="1.3" fill="#ffffff" />
      <circle cx="58.8" cy="56" r="1.3" fill="#ffffff" />
      <rect x="40" y="70" width="20" height="5" rx="2.5" fill="#db2777" />
    </template>

    <!-- 🌸 Fleur de cerisier -->
    <template v-else-if="emoji === '🌸'">
      <circle cx="50" cy="30" r="14" fill="#f8a8c8" />
      <circle cx="70" cy="44" r="14" fill="#f8a8c8" />
      <circle cx="63" cy="68" r="14" fill="#f8a8c8" />
      <circle cx="37" cy="68" r="14" fill="#f8a8c8" />
      <circle cx="30" cy="44" r="14" fill="#f8a8c8" />
      <circle cx="50" cy="52" r="10" fill="#fbd3e2" />
      <circle cx="50" cy="52" r="5" fill="#fbbf24" />
      <circle cx="88" cy="18" r="4" fill="#c4b5fd" />
    </template>

    <!-- 🌻 Tournesol -->
    <template v-else-if="emoji === '🌻'">
      <g fill="#fbbf24">
        <circle cx="50" cy="20" r="10" /><circle cx="68" cy="28" r="10" />
        <circle cx="78" cy="48" r="10" /><circle cx="70" cy="68" r="10" />
        <circle cx="50" cy="78" r="10" /><circle cx="30" cy="68" r="10" />
        <circle cx="22" cy="48" r="10" /><circle cx="32" cy="28" r="10" />
      </g>
      <circle cx="50" cy="48" r="17" fill="#8a5a2b" />
      <circle cx="44" cy="44" r="3" fill="#ffffff" />
      <circle cx="56" cy="44" r="3" fill="#ffffff" />
      <path d="M44 54 Q50 59 56 54" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🌈 Arc-en-ciel -->
    <template v-else-if="emoji === '🌈'">
      <path d="M16 70 A34 34 0 0 1 84 70" stroke="#f87171" stroke-width="9" fill="none" />
      <path d="M25 70 A25 25 0 0 1 75 70" stroke="#fbbf24" stroke-width="9" fill="none" />
      <path d="M34 70 A16 16 0 0 1 66 70" stroke="#60a5fa" stroke-width="9" fill="none" />
      <circle cx="14" cy="74" r="9" fill="#ffffff" stroke="#e3ddf2" stroke-width="2" />
      <circle cx="24" cy="72" r="7" fill="#ffffff" stroke="#e3ddf2" stroke-width="2" />
      <circle cx="86" cy="74" r="9" fill="#ffffff" stroke="#e3ddf2" stroke-width="2" />
      <circle cx="76" cy="72" r="7" fill="#ffffff" stroke="#e3ddf2" stroke-width="2" />
    </template>

    <!-- 🦋 Papillon -->
    <template v-else-if="emoji === '🦋'">
      <circle cx="28" cy="38" r="15" fill="#a78bfa" />
      <circle cx="72" cy="38" r="15" fill="#a78bfa" />
      <circle cx="32" cy="64" r="11" fill="#f8a8d8" />
      <circle cx="68" cy="64" r="11" fill="#f8a8d8" />
      <circle cx="28" cy="38" r="5" fill="#c9e4ff" />
      <circle cx="72" cy="38" r="5" fill="#c9e4ff" />
      <ellipse cx="50" cy="52" rx="7" ry="18" fill="#3b2a6b" />
      <path d="M46 34 Q42 24 38 22 M54 34 Q58 24 62 22" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🐝 Abeille -->
    <template v-else-if="emoji === '🐝'">
      <ellipse cx="22" cy="34" rx="11" ry="7" transform="rotate(-30 22 34)" fill="#dbeafe" stroke="#93c5fd" stroke-width="2" />
      <ellipse cx="78" cy="34" rx="11" ry="7" transform="rotate(30 78 34)" fill="#dbeafe" stroke="#93c5fd" stroke-width="2" />
      <ellipse cx="50" cy="56" rx="28" ry="24" fill="#fbbf24" />
      <path d="M38 34 Q36 56 38 78 M52 33 Q50 56 52 79 M66 36 Q64 56 66 76" stroke="#3b2a6b" stroke-width="7" stroke-linecap="round" fill="none" />
      <path d="M80 64 L92 68" stroke="#3b2a6b" stroke-width="5" stroke-linecap="round" />
      <ellipse cx="41" cy="50" rx="4" ry="5" fill="#3b2a6b" />
      <ellipse cx="58" cy="50" rx="4" ry="5" fill="#3b2a6b" />
      <circle cx="39.8" cy="48" r="1.3" fill="#ffffff" />
      <circle cx="56.8" cy="48" r="1.3" fill="#ffffff" />
      <path d="M42 62 Q49 68 56 62" stroke="#3b2a6b" stroke-width="3" stroke-linecap="round" fill="none" />
    </template>

    <!-- 🐬 Dauphin -->
    <template v-else-if="emoji === '🐬'">
      <path d="M20 62 Q30 30 60 30 Q82 30 84 48 Q86 62 70 70 Q46 80 28 72 Q18 68 20 62 Z" fill="#7fa8d9" />
      <path d="M52 32 Q56 18 68 16 Q62 26 60 34 Z" fill="#5b82b5" />
      <path d="M46 74 Q44 86 36 90 Q44 88 52 82 Z" fill="#5b82b5" />
      <circle cx="66" cy="46" r="3.6" fill="#3b2a6b" />
      <circle cx="65" cy="45" r="1.2" fill="#ffffff" />
      <path d="M70 56 Q76 58 80 54" stroke="#3b2a6b" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <circle cx="42" cy="52" r="4" fill="#a8c4e8" />
      <circle cx="34" cy="58" r="3" fill="#a8c4e8" />
    </template>

    <!-- Repli : emoji brut -->
    <template v-else>
      <text x="50" y="70" font-size="56" text-anchor="middle">{{ emoji }}</text>
    </template>
  </svg>
</template>

<script setup>
defineProps({
  emoji: { type: String, required: true },
  taille: { type: Number, default: 40 },
})
</script>
