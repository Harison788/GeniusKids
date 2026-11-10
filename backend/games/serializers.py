from rest_framework import serializers

from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "pseudo", "jeu", "niveau", "points", "etoiles", "cree_le"]
