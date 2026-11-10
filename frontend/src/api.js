/* Accès à l'API Django (proxifiée par Vite en développement). */

const CLE_JETON = 'geniuskids-jeton'

/* Jeton anonyme du profil : le backend s'en sert pour retrouver l'enfant. */
export function jetonProfil() {
  let jeton = localStorage.getItem(CLE_JETON)
  if (!jeton) {
    jeton = crypto.randomUUID ? crypto.randomUUID() : `j-${Date.now()}-${Math.random().toString(16).slice(2)}`
    localStorage.setItem(CLE_JETON, jeton)
  }
  return jeton
}

function entetes(supplement = {}) {
  return { 'Content-Type': 'application/json', 'X-Profil-Jeton': jetonProfil(), ...supplement }
}

export default {
  async charger(jeu, niveau) {
    const reponse = await fetch(`/api/${jeu}/?niveau=${niveau}`)
    if (!reponse.ok) {
      throw new Error(`API indisponible (${reponse.status})`)
    }
    return reponse.json()
  },

  /* Liste dynamique des mini-jeux (modèle Game côté Django). */
  async chargerJeux() {
    const reponse = await fetch('/api/jeux/')
    if (!reponse.ok) throw new Error('API jeux indisponible')
    return reponse.json()
  },

  /* Profil de l'enfant : nom, étoiles, avatar, thème (créé à la 1re visite). */
  async chargerProfil() {
    const reponse = await fetch('/api/profil/', { headers: entetes() })
    if (!reponse.ok) throw new Error('API profil indisponible')
    return reponse.json()
  },

  async majProfil(donnees) {
    try {
      const reponse = await fetch('/api/profil/', {
        method: 'PATCH',
        headers: entetes(),
        body: JSON.stringify(donnees),
      })
      if (!reponse.ok) return null
      return reponse.json()
    } catch {
      return null // hors ligne : on garde la version locale
    }
  },

  async envoyerScore(donnees) {
    try {
      await fetch('/api/scores/', {
        method: 'POST',
        headers: entetes(),
        body: JSON.stringify(donnees),
      })
    } catch {
      // Pas grave : le score est déjà gardé en local.
    }
  },
}
