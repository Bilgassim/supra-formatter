# Guide de Contribution 🤝

Merci de l'intérêt que vous portez à **Supra-Formatter** ! Ce projet se veut simple, efficace et ouvert à tous.

## Comment ajouter un nouveau format ?

Si vous souhaitez ajouter un nouveau format de sortie (ex: JSON, XML, ou un format spécifique à un outil), suivez ces étapes :

1.  Ouvrez `core/converter.py`.
2.  Ajoutez votre nouveau template dans le dictionnaire `FORMATS`.
3.  Si le format nécessite une détection spécifique, mettez à jour la méthode `detect_format`.
4.  Si le format nécessite un parsing particulier, mettez à jour la méthode `parse_line`.

## Standards de Code

- Nous suivons la norme **PEP 8**.
- Chaque nouvelle fonction doit avoir une **docstring** claire.
- Si vous ajoutez une fonctionnalité, essayez d'ajouter un cas de test dans le dossier `tests/`.

## Processus de Pull Request

1.  Forkez le dépôt.
2.  Créez une branche descriptive (`git checkout -b feature-nouvelle-conversion`).
3.  Effectuez vos changements et commitez-les.
4.  Poussez votre branche et ouvrez une Pull Request vers la branche `main`.

---
Ensemble, créons le meilleur outil de formatage SSH !
