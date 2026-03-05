# Texas Hold'em Poker Hand Evaluator

Ce projet est un évaluateur de mains de poker (Texas Hold'em) développé en Python. Il permet de déterminer la meilleure main de 5 cartes parmi un ensemble de 7 cartes (2 cartes privées + 5 cartes communes).

## Fonctionnalités implémentées

L'évaluateur reconnaît actuellement les catégories suivantes (selon la hiérarchie officielle) :

- **High Card** (Haute Carte)
- **One Pair** (Paire)
- **Two Pair** (Double Paire)
- **Three of a Kind** (Brelan)
- **Four of a Kind** (Carré)

## Choix de conception

- **Best-of-7** : L'algorithme analyse 7 cartes et sélectionne systématiquement le meilleur sous-ensemble de 5 cartes (`chosen_five_cards`).
- **Ordre d'importance** : Pour faciliter le départage (tie-break), les 5 cartes retournées sont ordonnées par importance (ex: la paire d'abord, puis les kickers par ordre décroissant).
- **Stabilité** : Utilisation de `collections.Counter` pour une analyse robuste des fréquences de rangs.

## 🛠 Installation et Tests

Pour lancer la suite de tests unitaires :

```bash
pytest
```
