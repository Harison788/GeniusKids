"""URLs principales de l'API « Les Petits Génies »."""
from django.urls import include, path

urlpatterns = [
    path("api/", include("games.urls")),
]
