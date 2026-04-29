# 🚀 Supra-Formatter

**Supra-Formatter** est un outil "méga-formateur" conçu pour les ingénieurs sécurité et administrateurs système. Il permet de jongler entre les différents formats de listes SSH les plus répandus sans se soucier du format source.

L'outil **détecte automatiquement** le format de vos fichiers d'entrée (Standard, CSV ou GoSSH) et les convertit instantanément vers le format de votre choix.

## 🌟 Fonctionnalités

- **Auto-Détection** : Plus besoin de spécifier le format d'entrée.
- **Support Multi-Format** :
  - **Standard** : `user@ip password` (utilisé par la plupart des bots et scripts simples)
  - **CSV** : `ip,user,password` (idéal pour Excel ou l'analyse de données)
  - **GoSSH** : `ip host=ip user=user password=pass` (format d'inventaire optimisé pour GoSSH)
- **Extensibilité** : Architecture modulaire permettant d'ajouter de nouveaux formats facilement.

## 🛠 Installation

```bash
git clone https://github.com/Bilgassim/supra-formatter.git
cd supra-formatter
chmod +x main.py
```

## 🚀 Utilisation

La syntaxe est simple :
```bash
python3 main.py <fichier_source> -f <format_cible> -o <fichier_sortie>
```

### Exemples :

1. **Convertir vers GoSSH** (peu importe la source) :
   ```bash
   python3 main.py cibles.txt -f gossh -o inventory.txt
   ```

2. **Convertir vers CSV** pour analyse :
   ```bash
   python3 main.py bots.txt -f csv -o data.csv
   ```

3. **Convertir du CSV vers le format Standard** :
   ```bash
   python3 main.py data.csv -f standard -o raw_list.txt
   ```

## 🤝 Contribution

Les contributions sont les bienvenues ! 
1. Forkez le projet.
2. Créez votre branche (`git checkout -b feature/AmazingFeature`).
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Pushez la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

---
Développé avec ❤️ pour la communauté.
