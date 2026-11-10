"""Sème les 5 nouveaux jeux : piano, échecs, sudoku, mots croisés, langue."""

from django.db import migrations, models

JEUX = [
    {
        "slug": "piano",
        "title": "Piano",
        "description": "Joue et répète la mélodie !",
        "category": "musique",
        "emoji": "🎹",
        "couleur_carte": "#fbe0e8",
        "ordre": 7,
    },
    {
        "slug": "echecs",
        "title": "Échecs",
        "description": "Bats Milo aux échecs !",
        "category": "reflexion",
        "emoji": "♟️",
        "couleur_carte": "#dfe7f5",
        "ordre": 8,
    },
    {
        "slug": "sudoku",
        "title": "Sudoku",
        "description": "Complète la grille magique",
        "category": "reflexion",
        "emoji": "🧠",
        "couleur_carte": "#dcf3e3",
        "ordre": 9,
    },
    {
        "slug": "mots",
        "title": "Mots croisés",
        "description": "Trouve tous les mots cachés",
        "category": "langues",
        "emoji": "🔤",
        "couleur_carte": "#fdf0cc",
        "ordre": 10,
    },
    {
        "slug": "langue",
        "title": "Langue",
        "description": "Le français et l'anglais",
        "category": "langues",
        "emoji": "🌍",
        "couleur_carte": "#fde2ef",
        "ordre": 11,
    },
]


def PREMIER(jeux_meta, schema_editor):
    Game = jeux_meta.get_model("games", "Game")
    for donnees in JEUX:
        Game.objects.update_or_create(
            slug=donnees["slug"],
            defaults={**donnees, "actif": True},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0004_couleurs_maquette"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="category",
            field=models.CharField(
                choices=[
                    ("nombres", "Nombres"),
                    ("memoire", "Mémoire"),
                    ("creativite", "Créativité"),
                    ("musique", "Musique"),
                    ("reflexion", "Réflexion"),
                    ("langues", "Langues"),
                ],
                default="nombres",
                max_length=20,
            ),
        ),
        migrations.RunPython(PREMIER, migrations.RunPython.noop),
    ]
