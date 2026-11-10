from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Un mini-jeu affiché sur la page d'accueil (piloté depuis l'admin Django)."""

    CATEGORIES = [
        ("nombres", "Nombres"),
        ("memoire", "Mémoire"),
        ("creativite", "Créativité"),
    ]

    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="nombres")
    image_url = models.CharField(max_length=200, blank=True, default="")
    emoji = models.CharField(max_length=10, blank=True, default="🎲")
    couleur_carte = models.CharField(
        max_length=20, blank=True, default="#f3f0ff",
        help_text="Fond pastel de la carte (hex).",
    )
    actif = models.BooleanField(default=True)
    ordre = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["ordre", "id"]

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    """Profil enfant : rattaché au User Django quand il existe, sinon repéré
    par un jeton anonyme conservé dans le navigateur (jeu sans inscription)."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="profil"
    )
    jeton = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=40, blank=True, default="Petit curieux")
    etoiles = models.PositiveIntegerField(default=0)
    avatar = models.CharField(max_length=10, blank=True, default="🦊")
    avatar_nom = models.CharField(max_length=40, blank=True, default="Petit renard")
    theme = models.CharField(max_length=20, blank=True, default="violet")

    def __str__(self):
        return f"{self.nom} ({self.etoiles} étoiles)"


class Score(models.Model):
    """Score enregistré à la fin d'une partie."""

    profil = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="scores"
    )
    pseudo = models.CharField(max_length=40)
    jeu = models.CharField(max_length=30)
    niveau = models.PositiveSmallIntegerField()
    points = models.PositiveIntegerField()
    etoiles = models.PositiveSmallIntegerField(default=0)
    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return f"{self.pseudo} — {self.jeu} niv. {self.niveau} : {self.points} pts"
