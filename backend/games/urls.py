from django.urls import path

from . import views

urlpatterns = [
    path("quiz/", views.api_quiz),
    path("comptage/", views.api_comptage),
    path("memory/", views.api_memory),
    path("associations/", views.api_associations),
    path("kakuro/", views.api_kakuro),
    path("scores/", views.api_scores),
]
