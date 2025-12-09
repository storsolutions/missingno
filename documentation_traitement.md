# Documentation du Traitement des Données

Ce document décrit le processus de nettoyage et de transformation appliqué au jeu de données `fichier-de-donnees-numeriques-69202f25dea8b267811864.csv` avant son utilisation par les modèles d'IA. L'objectif est de préparer des données de haute qualité en gérant les valeurs manquantes, les outliers et les inconsistances.

## Processus de Nettoyage Réalisé par `process_data.py`

Le script `process_data.py` exécute les étapes suivantes :

### 1. Chargement des Données

*   **Action :** Le fichier `fichier-de-donnees-numeriques-69202f25dea8b267811864.csv` est chargé dans un DataFrame Pandas.
*   **Justification :** Point de départ pour toutes les opérations de traitement.

### 2. Suppression des Colonnes Quasi-Vides

*   **Action :** Les colonnes avec plus de **50% de valeurs manquantes** sont identifiées et supprimées.
    *   **Résultat :** Les colonnes `historique_credits` (52.93% manquantes) et `score_credit` (53.06% manquantes) ont été supprimées.
*   **Justification :** Conserver des colonnes avec un pourcentage aussi élevé de valeurs manquantes introduirait un bruit significatif ou nécessiterait une imputation massive qui pourrait biaiser fortement les analyses ultérieures. Un seuil de 50% est jugé approprié pour garantir que les colonnes restantes contiennent des informations substantielles.

### 3. Suppression des Lignes Trop Incomplètes

*   **Action :** Les lignes avec plus de **50% de valeurs manquantes** (après la suppression des colonnes quasi-vides) sont identifiées et supprimées.
    *   **Résultat :** Aucune ligne n'a dépassé ce seuil, ce qui signifie que le jeu de données ne contenait pas de lignes "trop incomplètes" selon ce critère après la suppression des colonnes.
*   **Justification :** Les lignes avec un grand nombre de valeurs manquantes sont souvent difficiles à imputer sans introduire de fortes distorsions et peuvent représenter des enregistrements de faible qualité. La suppression de ces lignes permet de maintenir l'intégrité du dataset pour les modèles. Le seuil de 50% a été choisi pour éliminer les enregistrements gravement déficients.

### 4. Correction des Outliers Évidents

*   **Action :**
    *   Les valeurs négatives dans la colonne `loyer_mensuel` sont corrigées en prenant leur valeur absolue.
    *   Les valeurs extrêmes (outliers) dans les colonnes `montant_pret` et `revenu_estime_mois` sont "clippées" (plafonnées) au **99ème percentile**.
*   **Justification :**
    *   **`loyer_mensuel` négatif :** Un loyer négatif est une incohérence manifeste et très probablement une erreur de saisie de données. La prise de la valeur absolue est une correction simple et directe pour ramener ces valeurs dans un domaine sémantiquement correct.
    *   **`montant_pret` et `revenu_estime_mois` :** Les outliers dans ces colonnes peuvent fausser les calculs de moyenne/médiane et affecter la performance des modèles. Le clipping au 99ème percentile est une méthode robuste qui réduit l'impact des valeurs extrêmes sans les supprimer entièrement, ce qui pourrait entraîner une perte d'information. Il permet de conserver la majeure partie de la distribution tout en atténuant l'influence des valeurs aberrantes qui pourraient être des erreurs de mesure ou des cas exceptionnels rares.

### 5. Imputation des Valeurs NULL/NaN Restantes

*   **Action :** Toutes les valeurs `NULL`/`NaN` restantes dans les colonnes numériques sont imputées en utilisant la **médiane** de chaque colonne respective.
    *   **Résultat :** Les valeurs manquantes dans la colonne `loyer_mensuel` ont été imputées avec la médiane.
*   **Justification :** La médiane est choisie pour l'imputation car, contrairement à la moyenne, elle est **robuste aux outliers**. Étant donné que nous avons déjà identifié et traité des outliers (ou du moins leurs impacts), l'imputation par la médiane est une approche prudente qui minimise la distorsion de la distribution de la colonne, surtout si des outliers résiduels ou subtils persistent après le clipping.

### 6. Sauvegarde des Données Nettoyées

*   **Action :** Le DataFrame traité est sauvegardé dans un nouveau fichier CSV nommé `donnees_nettoyees.csv`.
*   **Justification :** Permet de disposer d'une version propre et prête à l'emploi des données, distincte du fichier original.

Ce processus garantit un jeu de données plus cohérent et fiable pour les analyses ultérieures et l'entraînement des modèles d'IA.
