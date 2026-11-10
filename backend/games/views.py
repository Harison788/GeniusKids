"""Générateurs d'activités et scores pour les petits curieux.

Trois niveaux, de 4 à 11 ans :
  - niveau 1 (Écureuil 🐿️)  : 4-6 ans, additions jusqu'à 10, dénombrement ;
  - niveau 2 (Renard 🦊)     : 6-8 ans, +/- jusqu'à 20, tables de 2, 5, 10 ;
  - niveau 3 (Hibou 🦉)      : 9-11 ans, toutes les tables, divisions, suites.
"""

import random
import uuid

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game, Score, UserProfile
from .serializers import GameSerializer, ProfilSerializer, ScoreSerializer

NIVEAUX_VALIDES = {1, 2, 3}
NOMBRE_PAR_DEFAUT = 8

EMOJIS = ["🍎", "🍓", "🐝", "⚽", "🎈", "🌻", "🐠", "🚗"]

FORMES = [
    ("Carré", "⬛"),
    ("Cercle", "🔵"),
    ("Triangle", "🔺"),
    ("Étoile", "⭐"),
    ("Cœur", "❤️"),
]

NOMS_NOMBRES = [
    "zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
    "huit", "neuf", "dix", "onze", "douze",
]


# ---------------------------------------------------------------------------
# Petites fonctions utilitaires
# ---------------------------------------------------------------------------

def _niveau(request):
    try:
        niveau = int(request.query_params.get("niveau", 1))
    except (TypeError, ValueError):
        niveau = 1
    return niveau if niveau in NIVEAUX_VALIDES else 1


def _nombre(request):
    """Nombre de questions demandé (serré entre 1 et 20)."""
    try:
        nombre = int(request.query_params.get("nombre", NOMBRE_PAR_DEFAUT))
    except (TypeError, ValueError):
        nombre = NOMBRE_PAR_DEFAUT
    return max(1, min(nombre, 20))


def _distracteurs(bonne_reponse, amplitude=4, mini=0, nombre=3):
    """Trois mauvaises réponses plausibles, positives si possible."""
    propositions = set()
    essais = 0
    while len(propositions) < nombre and essais < 200:
        essais += 1
        delta = random.randint(1, max(2, amplitude))
        if random.random() < 0.5:
            delta = -delta
        candidat = bonne_reponse + delta
        if candidat >= mini and candidat != bonne_reponse:
            propositions.add(candidat)
    while len(propositions) < nombre:  # sécurité
        propositions.add(bonne_reponse + len(propositions) + amplitude + 1)
    choix = sorted(propositions)[:nombre] + [bonne_reponse]
    random.shuffle(choix)
    return choix


# ---------------------------------------------------------------------------
# Quiz de mathématiques
# ---------------------------------------------------------------------------

def _calcul(niveau):
    """Retourne un énoncé (texte, bonne réponse) adapté au niveau."""
    if niveau == 1:
        a, b = random.randint(1, 5), random.randint(1, 5)
        return f"{a} + {b}", a + b

    if niveau == 2:
        operation = random.choice(["+", "-", "x"])
        if operation == "+":
            a, b = random.randint(2, 12), random.randint(2, 12)
            return f"{a} + {b}", a + b
        if operation == "-":
            a, b = random.randint(5, 20), random.randint(1, 5)
            return f"{a} - {b}", a - b
        a = random.choice([2, 5, 10])
        b = random.randint(1, 9)
        return f"{a} x {b}", a * b

    # niveau 3
    if random.random() < 0.7:
        a, b = random.randint(2, 10), random.randint(2, 10)
        return f"{a} x {b}", a * b
    diviseur = random.randint(2, 10)
    quotient = random.randint(2, 10)
    return f"{diviseur * quotient} ÷ {diviseur}", quotient


def _questions_quiz(niveau, nombre):
    questions = []
    for _ in range(nombre):
        question, reponse = _calcul(niveau)
        questions.append({
            "question": question,
            "reponse": reponse,
            "choix": _distracteurs(reponse, amplitude=max(3, reponse // 2)),
        })
    return questions


@api_view(["GET"])
def api_quiz(request):
    niveau = _niveau(request)
    return Response({
        "jeu": "quiz",
        "niveau": niveau,
        "questions": _questions_quiz(niveau, _nombre(request)),
    })


# ---------------------------------------------------------------------------
# Comptage et nombres manquants
# ---------------------------------------------------------------------------

def _question_comptage(niveau):
    if niveau == 1:
        if random.random() < 0.5:
            emoji = random.choice(EMOJIS)
            quantite = random.randint(1, 9)
            return {
                "question": "Compte : combien il y en a ?",
                "affichage": " ".join([emoji] * quantite),
                "reponse": quantite,
                "choix": _distracteurs(quantite, amplitude=3),
            }
        depart = random.randint(1, 8)
        return {
            "question": f"Quel nombre vient après {depart} ?",
            "affichage": "",
            "reponse": depart + 1,
            "choix": _distracteurs(depart + 1, amplitude=3),
        }

    if niveau == 2:
        debut = random.randint(1, 6)
        bond = random.choice([1, 2, 3])
        question = "Quel nombre manque dans la suite ?"
    else:
        debut = random.choice([2, 3, 4, 5])
        bond = random.randint(3, 6)
        question = "Continue la suite : quel nombre manque ?"

    suite = [debut + bond * i for i in range(5)]
    position_cachee = random.randrange(1, 4)
    bonne = suite[position_cachee]
    visible = [str(valeur) if i != position_cachee else "?"
               for i, valeur in enumerate(suite)]
    return {
        "question": question,
        "affichage": " • ".join(visible),
        "reponse": bonne,
        "choix": _distracteurs(bonne, amplitude=bond + 2),
    }


@api_view(["GET"])
def api_comptage(request):
    niveau = _niveau(request)
    return Response({
        "jeu": "comptage",
        "niveau": niveau,
        "questions": [_question_comptage(niveau) for _ in range(_nombre(request))],
    })


# ---------------------------------------------------------------------------
# Memory : trouver les cartes qui vont ensemble
# ---------------------------------------------------------------------------

def _deck_memory(niveau, nombre_paires=6):
    style = "emoji" if (niveau == 1 and random.random() < 0.5) else "calcul"
    paires = []
    valeurs_utilisees = set()
    essais = 0
    while len(paires) < nombre_paires and essais < 300:
        essais += 1
        if style == "emoji":
            emoji = random.choice(EMOJIS)
            valeur = random.randint(1, 6)
            gauche = " ".join([emoji] * valeur)
        else:
            gauche, valeur = _calcul(niveau)
        if valeur in valeurs_utilisees or any(p["gauche"] == gauche for p in paires):
            continue
        valeurs_utilisees.add(valeur)
        paires.append({"gauche": gauche, "droite": str(valeur)})
    for numero, paire in enumerate(paires):
        paire["id"] = numero
    random.shuffle(paires)
    return paires


@api_view(["GET"])
def api_memory(request):
    niveau = _niveau(request)
    return Response({
        "jeu": "memory",
        "niveau": niveau,
        "paires": _deck_memory(niveau),
    })


# ---------------------------------------------------------------------------
# Associations : relier ce qui va ensemble
# ---------------------------------------------------------------------------

def _paires_associations(niveau):
    """Retourne (titre, liste de paires {gauche, droite})."""
    if niveau == 1:
        if random.random() < 0.5:
            nombres = random.sample(range(1, 7), 4)
            return "Chiffres et quantités 🍬", [
                {"gauche": str(n), "droite": " ".join(["🍬"] * n)}
                for n in nombres
            ]
        formes = random.sample(FORMES, 4)
        return "Les formes ✏️", [
            {"gauche": nom, "droite": emoji} for nom, emoji in formes
        ]

    if niveau == 2:
        if random.random() < 0.5:
            paires, valeurs = [], set()
            while len(paires) < 4:
                question, valeur = _calcul(2)
                if valeur in valeurs:
                    continue
                valeurs.add(valeur)
                paires.append({"gauche": question, "droite": str(valeur)})
            return "Petits calculs ➕", paires
        nombres = random.sample(range(1, 13), 4)
        return "Nombres en lettres 🔤", [
            {"gauche": str(n), "droite": NOMS_NOMBRES[n]}
            for n in nombres
        ]

    # niveau 3
    if random.random() < 0.5:
        valeurs = random.sample(range(10, 100), 4)
        return "Compléments à 100 💯", [
            {"gauche": str(v), "droite": str(100 - v)}
            for v in valeurs
        ]
    nombres_parts = random.sample(range(2, 7), 4)
    return "Fractions et pizzas 🍕", [
        {"gauche": f"Pizza en {p} parts", "droite": f"1/{p}"}
        for p in nombres_parts
    ]


@api_view(["GET"])
def api_associations(request):
    niveau = _niveau(request)
    titre, paires_brutes = _paires_associations(niveau)
    paires = []
    for numero, paire in enumerate(paires_brutes):
        paires.append({
            "id": numero,
            "gauche": paire["gauche"],
            "droite": paire["droite"],
        })
    return Response({
        "jeu": "associations",
        "niveau": niveau,
        "theme": titre,
        "paires": paires,
    })


# ---------------------------------------------------------------------------
# Kakuro : lignes et colonnes dont la somme est donnée
# ---------------------------------------------------------------------------

KAKURO_TAILLES = {1: 2, 2: 3, 3: 4}


def _matrixe_kakuro(taille):
    """Matrice solution : chiffres distincts dans chaque ligne ET colonne."""
    essais = 0
    while essais < 400:
        essais += 1
        rangees = [random.sample(range(1, 10), taille) for _ in range(taille)]
        colonnes_distinctes = all(
            len({rangee[col] for rangee in rangees}) == taille
            for col in range(taille)
        )
        if colonnes_distinctes:
            return rangees
    # Filet de sécurité : carré latin par rotation (toujours valide).
    base = sorted(random.sample(range(1, 10), taille))
    return [base[i:] + base[:i] for i in range(taille)]


@api_view(["GET"])
def api_kakuro(request):
    niveau = _niveau(request)
    taille = KAKURO_TAILLES.get(niveau, 2)
    solution = _matrixe_kakuro(taille)
    return Response({
        "jeu": "kakuro",
        "niveau": niveau,
        "taille": taille,
        "cibleLignes": [sum(rangee) for rangee in solution],
        "cibleColonnes": [sum(rangee[col] for rangee in solution) for col in range(taille)],
        "solution": solution,
    })


# ---------------------------------------------------------------------------
# Catalogue des jeux (liste dynamique pilotée par le modèle Game)
# ---------------------------------------------------------------------------

@api_view(["GET"])
def api_jeux(request):
    jeux = Game.objects.filter(actif=True)
    categorie = request.query_params.get("categorie")
    if categorie:
        jeux = jeux.filter(category=categorie)
    return Response(GameSerializer(jeux, many=True).data)


# ---------------------------------------------------------------------------
# Profil enfant (nom, étoiles, avatar, thème) — sans inscription obligatoire.
# Le navigateur envoie son jeton (en-tête X-Profil-Jeton) ; le profil est
# créé à la première visite. Si un User Django est authentifié, le profil
# est rattaché à son compte.
# ---------------------------------------------------------------------------

def _utilisateur(request):
    """Le User Django connecté, ou None (les enfants jouent sans compte)."""
    user = getattr(request, "user", None)
    return user if getattr(user, "is_authenticated", False) else None


def _profil_depuis_requete(request):
    jeton = request.headers.get("X-Profil-Jeton", "")
    profil = None
    if jeton:
        profil = UserProfile.objects.filter(jeton=jeton).first()
    if profil is None:
        jeton = jeton or uuid.uuid4().hex
        profil = UserProfile.objects.create(
            jeton=jeton,
            user=_utilisateur(request),
        )
    elif request.user is not None and profil.user is None:
        utilisateur = _utilisateur(request)
        if utilisateur is not None:
            profil.user = utilisateur
            profil.save()
    return profil


@api_view(["GET", "PATCH"])
def api_profil(request):
    profil = _profil_depuis_requete(request)

    if request.method == "PATCH":
        serializer = ProfilSerializer(profil, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    reponse = Response(ProfilSerializer(profil).data)
    reponse["X-Profil-Jeton"] = profil.jeton
    return reponse


# ---------------------------------------------------------------------------
# Scores (profil simple, sans inscription)
# ---------------------------------------------------------------------------

@api_view(["GET", "POST"])
def api_scores(request):
    if request.method == "POST":
        serializer = ScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        score = serializer.save()
        jeton = request.headers.get("X-Profil-Jeton", "")
        if jeton:
            profil = UserProfile.objects.filter(jeton=jeton).first()
            if profil:
                score.profil = profil
                score.save(update_fields=["profil"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    queryset = Score.objects.all()
    pseudo = request.query_params.get("pseudo")
    if pseudo:
        queryset = queryset.filter(pseudo=pseudo)
    queryset = queryset.order_by("-points")[:50]
    return Response(ScoreSerializer(queryset, many=True).data)
