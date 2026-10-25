<h1 align="center">🔗 PageRank</h1>

<p align="center"><em>L'algorithme de classement popularisé par Google, en version mini. Classe tes pages par importance.</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3" />
  <img src="https://img.shields.io/badge/d%C3%A9pendances-numpy-orange?style=for-the-badge" alt="NumPy" />
  <img src="https://img.shields.io/badge/projet%20d%27apprentissage-ff69b4?style=for-the-badge" alt="Projet d'apprentissage" />
</p>

---

## ✨ Pourquoi tu vas l'adorer

- **Calcul matriciel** avec NumPy : tous les scores sont mis à jour en une seule opération.
- **Arrêt automatique** : le calcul s'arrête dès que les scores ne bougent presque plus (seuil de 0,01).
- **Classement lisible** : la page choisie s'affiche en premier, suivie des autres par ordre d'importance.

## 📥 Format des données

Le programme lit, dans l'ordre :

1. le nombre de pages ;
2. les noms des pages, séparés par des espaces ;
3. la matrice des liens, une ligne par page ;
4. la page à afficher en premier.

Exemple avec trois pages :

```text
3
A B C
0 1 0
1 0 1
0 1 0
B
```

## 🚀 Lancer

```bash
pip install numpy
python3 PageRank.py
```

## 🧠 Sous le capot

- Le facteur d'amortissement vaut `0.5` : à chaque étape, on suit un lien une fois sur deux, sinon on « saute » vers une page au hasard.
- Les scores sont recalculés avec `r = M · r` jusqu'à ce que deux itérations successives ne diffèrent presque plus.
- `numpy.linalg.norm` mesure cette différence entre deux itérations.

## 🔭 Pistes d'évolution

- Normaliser les scores pour obtenir de vraies probabilités : leur somme n'est pas conservée aujourd'hui.
- Rendre le facteur d'amortissement réglable depuis l'entrée.

---

<p align="center"><sub>Fait avec ❤️ et Python par DSKarim</sub></p>
