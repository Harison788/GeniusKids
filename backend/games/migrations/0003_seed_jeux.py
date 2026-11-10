"""Insère les 6 jeux de la maquette dans la table Game."""

from django.db import migrations

JEUX_DEPART = [
    {
        "title": "Quiz Maths",
        "slug": "quiz",
        "description": "Joue avec les nombres",
        "category": "nombres",
        "emoji": "➕",
        "couleur_carte": "#f3f0ff",
        "ordre": 1,
    },
    {
        "title": "Memory",
        "slug": "memory",
        "description": "Trouve les paires",
        "category": "memoire",
        "emoji": "⭐",
        "couleur_carte": "#e9e4fb",
        "ordre": 2,
    },
    {
        "title": "Fusion des fruits",
        "slug": "fruits",
        "description": "Fais le plein de fruits !",
        "category": "creativite",
        "emoji": "🍑",
        "couleur_carte": "#fdeedd",
        "ordre": 3,
    },
    {
        "title": "Puzzles",
        "slug": "puzzle",
        "description": "Assemble et découvre",
        "category": "creativite",
        "emoji": "🧩",
        "couleur_carte": "#ddf2e9",
        "ordre": 4,
    },
    {
        "title": "Kakuro",
        "slug": "kakuro",
        "description": "À toi de calculer !",
        "category": "nombres",
        "emoji": "🔢",
        "couleur_carte": "#e9e4fb",
        "ordre": 5,
    },
    {
        "title": "Comptage",
        "slug": "comptage",
        "description": "Compte avec nous",
        "category": "nombres",
        "emoji": "🧮",
        "couleur_carte": "#fef3c7",
        "ordre": 6,
    },
]


def seed(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    for donnees in JEUX_DEPART:
        Game.objects.get_or_create(slug=donnees["slug"], defaults=donnees)


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_game_userprofile_score_profil"),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
