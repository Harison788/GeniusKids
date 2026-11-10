"""Ajuste les couleurs des cartes des jeux pour coller à la maquette."""

from django.db import migrations

COULEURS = {
    "quiz": "#e3d7fa",
    "memory": "#ded9fb",
    "fruits": "#fbe3d3",
    "puzzle": "#d9f0e6",
    "kakuro": "#ddd5fa",
    "comptage": "#fdf2cc",
}


def MAJ(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    for slug, couleur in COULEURS.items():
        Game.objects.filter(slug=slug).update(couleur_carte=couleur)


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_seed_jeux"),
    ]

    operations = [
        migrations.RunPython(MAJ, migrations.RunPython.noop),
    ]
