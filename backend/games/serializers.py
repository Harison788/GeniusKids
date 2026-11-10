from rest_framework import serializers

from .models import Game, Score, UserProfile


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "title", "slug", "description", "category", "image_url", "emoji", "couleur_carte"]


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["jeton", "nom", "etoiles", "avatar", "avatar_nom", "theme"]
        read_only_fields = ["jeton"]


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "pseudo", "jeu", "niveau", "points", "etoiles", "cree_le"]
