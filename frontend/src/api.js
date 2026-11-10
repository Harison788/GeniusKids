/* Accès à l'API Django (proxifiée par Vite en développement). */
export default {
  async charger(jeu, niveau) {
    const reponse = await fetch(`/api/${jeu}/?niveau=${niveau}`)
    if (!reponse.ok) {
      throw new Error(`API indisponible (${reponse.status})`)
    }
    return reponse.json()
  },
  async envoyerScore(donnees) {
    try {
      await fetch('/api/scores/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(donnees),
      })
    } catch {
      // Pas grave : le score est déjà gardé en local.
    }
  },
}
