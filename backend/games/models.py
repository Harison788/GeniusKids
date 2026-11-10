from django.db import models


class Score(models.Model):
    """Score enregistré à la fin d'une partie (profil simple, sans inscription)."""

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
