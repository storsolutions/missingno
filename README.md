# Projet d'Analyse et de Nettoyage de Données Numériques

Ce dépôt contient le processus complet d'analyse exploratoire, de nettoyage, de transformation et de documentation d'un jeu de données numériques. L'objectif est de préparer des données de haute qualité pour l'utilisation par des modèles d'intelligence artificielle.

## Structure du Dépôt

*   `fichier-de-donnees-numeriques-69202f25dea8b267811864.csv` : Le jeu de données original fourni.
*   `donnees_nettoyees.csv` : Le jeu de données après le processus de nettoyage.
*   `process_data.py` : Script Python contenant le processus de nettoyage et de transformation des données.
*   `analyse_statistique.py` : Script Python pour comparer statistiquement et visuellement les données avant et après le nettoyage.
*   `documentation_traitement.md` : Documentation détaillée justifiant les choix effectués lors du nettoyage des données.
*   `README.md` : Ce fichier, présentant le projet et sa structure.

### Dossier `visualisations/` (à créer ou contenir les images générées)

Ce dossier contiendra toutes les visualisations générées lors de l'analyse exploratoire initiale et de la comparaison avant/après nettoyage.

*   `nullity_matrix.png`
*   `nullity_bar_chart.png`
*   `nullity_heatmap.png`
*   `boxplot_*.png` (un pour chaque colonne numérique)
*   `distribution_*.png` (un pour chaque colonne numérique, avant nettoyage)
*   `distribution_comparison_*.png` (comparaison avant/après nettoyage pour chaque colonne numérique)
*   `pairplot_numerical_features.png`

## Processus de Traitement

Le processus de traitement des données suit les étapes suivantes :

1.  **Analyse Exploratoire Initiale :** Identification des valeurs manquantes, détection des outliers et visualisation des distributions et relations entre les features. Les scripts `analyze_missing_values.py`, `analyze_outliers.py`, et `analyze_distributions_relations.py` (qui ont été exécutés et leurs sorties sont les images `*.png` mentionnées ci-dessus) ont permis cette étape.
2.  **Nettoyage des Données :** Application de règles de suppression de colonnes/lignes, correction des outliers et imputation des valeurs manquantes. Ce processus est détaillé dans `process_data.py`.
3.  **Documentation :** Chaque décision prise durant le nettoyage est justifiée dans `documentation_traitement.md`.
4.  **Analyse Statistique Avant/Après :** Comparaison des propriétés statistiques et des distributions des données originales et nettoyées, effectuée par `analyse_statistique.py`.

## Comment Exécuter les Scripts

Pour exécuter les scripts et reproduire l'analyse et le nettoyage :

1.  Assurez-vous d'avoir Python installé.
2.  Installez les bibliothèques nécessaires :
    ```bash
    pip install pandas numpy matplotlib seaborn missingno tabulate
    ```
3.  Exécutez le script de nettoyage des données :
    ```bash
    python process_data.py
    ```
    Cela générera le fichier `donnees_nettoyees.csv`.

4.  Exécutez le script d'analyse statistique :
    ```bash
    python analyse_statistique.py
    ```
    Cela affichera les statistiques descriptives et générera les graphiques de comparaison.

## Auteur

[Votre Nom/Pseudo]
[Date]

---
**Note :** Les images des visualisations générées ne sont pas directement incluses dans ce `README.md` mais sont sauvegardées en tant que fichiers `.png` dans le dossier `visualisations/` après exécution des scripts correspondants.
