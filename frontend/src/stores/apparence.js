/* Apparence de l'enfant : avatar et thème visuel.
   Synchronisée avec le profil Django (UserProfile) via l'API. */
import { reactive } from 'vue'
import API from '../api'

const CLE = 'geniuskids-apparence'

/* --- Avatars : l'enfant choisit qui il veut être --- */
export const AVATARS = [
  {
    groupe: 'Les animaux',
    liste: [
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
    ],
  },
  {
    groupe: 'Les personnages',
    liste: [
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
    ],
  },
  {
    groupe: 'La nature et les fleurs',
    liste: [
      { emoji: '🌸', nom: 'Fleur de cerisier' },
      { emoji: '🌻', nom: 'Grand tournesol' },
      { emoji: '🌈', nom: 'Arc-en-ciel' },
      { emoji: '🦋', nom: 'Papillon' },
      { emoji: '🐝', nom: 'Petite abeille' },
      { emoji: '🐬', nom: 'Dauphin' },
    ],
  },
]

/* --- Thèmes : le décor autour des jeux. Le blanc/violet est celui de départ. ---
   `apercu` = petit dégradé fidèle au décor réel, montré dans la modale. */
export const THEMES = [
  { id: 'violet', nom: 'Violet doux', emoji: '🟣', apercu: 'linear-gradient(160deg, #ffffff, #f3f0ff)' },
  { id: 'fleurs', nom: 'Jardin de fleurs', emoji: '🌸', apercu: 'linear-gradient(160deg, #fff1f7, #fbcfe8)' },
  { id: 'voitures', nom: 'Monde des voitures', emoji: '🚗', apercu: 'linear-gradient(160deg, #eaf2fd, #404a5a)' },
  { id: 'espace', nom: 'Espace étoilé', emoji: '🚀', apercu: 'linear-gradient(160deg, #eef1ff, #a5b4fc)' },
  { id: 'ocean', nom: 'Fond des océans', emoji: '🐠', apercu: 'linear-gradient(160deg, #e3f6fc, #99e3f5)' },
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

/* Envoie l'apparence au backend (sans bloquer l'interface). */
function synchroniser() {
  API.majProfil({
    avatar: apparence.avatar,
    avatar_nom: apparence.avatarNom,
    theme: apparence.theme,
  })
}

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
  synchroniser()
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
  synchroniser()
}

export function themeActuel() {
  return THEMES.find((t) => t.id === apparence.theme) ?? THEMES[0]
}

/* Charge l'apparence depuis le profil Django (au démarrage de l'app). */
export async function chargerApparenceDistante() {
  try {
    const profil = await API.chargerProfil()
    if (profil.avatar && profil.avatar !== apparence.avatar) {
      const connu = trouverAvatar(profil.avatar)
      apparence.avatar = connu.emoji
      apparence.avatarNom = profil.avatar_nom || connu.nom
    }
    if (profil.theme) apparence.theme = profil.theme
    enregistrerApparence()
    return profil
  } catch {
    return null // backend éteint : on joue en local
  }
}
