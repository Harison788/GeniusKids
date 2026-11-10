/* Apparence de l'enfant : avatar et thème visuel, gardés dans le navigateur. */
import { reactive } from 'vue'

const CLE = 'geniuskids-apparence'

/* --- Avatars : l'enfant choisit qui il veut être --- */
export const AVATARS = [
  { groupe: 'Les animaux', liste: [
    { emoji: '🦊', nom: 'Petit renard' },
    { emoji: '🐱', nom: 'Petit chat' },
    { emoji: '🐶', nom: 'Petit chien' },
    { emoji: '🐼', nom: 'Petit panda' },
    { emoji: '🐰', nom: 'Petit lapin' },
    { emoji: '🦁', nom: 'Petit lion' },
    { emoji: '🐸', nom: 'Petite grenouille' },
    { emoji: '🦉', nom: 'Petit hibou' },
    { emoji: '🐙', nom: 'Petite pieuvre' },
    { emoji: '🦄', nom: 'Petite licorne' },
    { emoji: '🐢', nom: 'Petite tortue' },
  ] },
  { groupe: 'Les personnages', liste: [
    { emoji: '👦', nom: 'Petit garçon' },
    { emoji: '👧', nom: 'Petite fille' },
    { emoji: '🦸‍♂️', nom: 'Super héros' },
    { emoji: '🦸‍♀️', nom: 'Super héroïne' },
    { emoji: '🧑‍🚀', nom: 'Astronaute' },
    { emoji: '🧚‍♀️', nom: 'Petite fée' },
    { emoji: '🤴', nom: 'Prince' },
    { emoji: '👸', nom: 'Princesse' },
    { emoji: '🧙‍♂️', nom: 'Petit magicien' },
    { emoji: '🥷', nom: 'Petit ninja' },
  ] },
  { groupe: 'La nature et les fleurs', liste: [
    { emoji: '🌸', nom: 'Fleur de cerisier' },
    { emoji: '🌻', nom: 'Grand tournesol' },
    { emoji: '🌈', nom: 'Arc-en-ciel' },
    { emoji: '🦋', nom: 'Papillon' },
    { emoji: '🐝', nom: 'Petite abeille' },
    { emoji: '🐬', nom: 'Dauphin' },
  ] },
]

/* --- Thèmes : le décor autour des jeux. Le violet est celui de départ. --- */
export const THEMES = [
  { id: 'violet', nom: 'Violet doux', emoji: '🟣', apercu: '#efe7fd' },
  { id: 'fleurs', nom: 'Jardin de fleurs', emoji: '🌸', apercu: '#fde9f1' },
  { id: 'voitures', nom: 'Monde des voitures', emoji: '🚗', apercu: '#e6eef8' },
  { id: 'espace', nom: 'Espace étoilé', emoji: '🚀', apercu: '#e3e6ff' },
  { id: 'ocean', nom: 'Fond des océans', emoji: '🐠', apercu: '#e2f6fb' },
]

function vide() {
  return { avatar: '🦊', avatarNom: 'Petit renard', theme: 'violet' }
}

function charger() {
  try {
    const brut = JSON.parse(localStorage.getItem(CLE))
    return brut && typeof brut === 'object' ? { ...vide(), ...brut } : vide()
  } catch {
    return vide()
  }
}

export const apparence = reactive(charger())

export function enregistrerApparence() {
  try {
    localStorage.setItem(CLE, JSON.stringify(apparence))
  } catch {
    // Stockage indisponible (mode privé) : on continue sans sauvegarde.
  }
}

export function choisirAvatar(avatar) {
  apparence.avatar = avatar.emoji
  apparence.avatarNom = avatar.nom
  enregistrerApparence()
}

export function trouverAvatar(emoji) {
  for (const groupe of AVATARS) {
    const trouve = groupe.liste.find((a) => a.emoji === emoji)
    if (trouve) return trouve
  }
  return AVATARS[0].liste[0]
}

export function choisirTheme(id) {
  apparence.theme = THEMES.some((t) => t.id === id) ? id : 'violet'
  enregistrerApparence()
}

export function themeActuel() {
  return THEMES.find((t) => t.id === apparence.theme) ?? THEMES[0]
}
