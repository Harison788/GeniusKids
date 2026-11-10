/* Le service worker ne s'active qu'en production (build) :
   en développement, il servait des pages vieilles via le cache
   et provoquait des pages blanches après chaque refactor. */
export function enregistrerServiceWorker() {
  if (!('serviceWorker' in navigator)) return
  if (import.meta.env.DEV) return

  navigator.serviceWorker.register('/sw.js').catch(() => {
    // Installation impossible (non-HTTPS, etc.) : l'app marche quand même.
  })
}
