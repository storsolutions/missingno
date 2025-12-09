
import pandas as pd
import numpy as np

def clean_data(input_file='fichier-de-donnees-numeriques-69202f25dea8b267811864.csv', output_file='donnees_nettoyees.csv'):
    """
    This script cleans the provided dataset by:
    1. Removing columns with a high percentage of missing values.
    2. Removing rows with a high percentage of missing values.
    3. Correcting obvious outliers.
    4. Imputing remaining missing values.
    """
    print(f"Chargement des données depuis {input_file}...")
    df = pd.read_csv(input_file)
    print("Données initiales chargées. Shape:", df.shape)

    # --- 1. Supprimer les colonnes quasi-vides ---
    print("\n--- Étape 1: Suppression des colonnes quasi-vides ---")
    missing_col_percent = df.isnull().sum() / len(df) * 100
    print("Pourcentage de valeurs manquantes par colonne:\n", missing_col_percent)
    
    threshold_col = 50.0
    cols_to_drop = missing_col_percent[missing_col_percent > threshold_col].index
    
    if len(cols_to_drop) > 0:
        df.drop(columns=cols_to_drop, inplace=True)
        print(f"\nColonnes supprimées (plus de {threshold_col}% de valeurs manquantes): {list(cols_to_drop)}")
    else:
        print("\nAucune colonne ne dépasse le seuil de valeurs manquantes.")
    print("Shape après suppression des colonnes:", df.shape)

    # --- 2. Supprimer les lignes trop incomplètes ---
    print("\n--- Étape 2: Suppression des lignes trop incomplètes ---")
    missing_row_percent = df.isnull().sum(axis=1) / df.shape[1] * 100
    
    threshold_row = 50.0
    rows_to_drop = missing_row_percent[missing_row_percent > threshold_row].index
    
    if len(rows_to_drop) > 0:
        df.drop(index=rows_to_drop, inplace=True)
        print(f"\nLignes supprimées (plus de {threshold_row}% de valeurs manquantes): {len(rows_to_drop)} lignes")
    else:
        print("\nAucune ligne ne dépasse le seuil de valeurs manquantes.")
    print("Shape après suppression des lignes:", df.shape)

    # --- 3. Détecter et corriger les outliers ---
    print("\n--- Étape 3: Correction des outliers ---")
    # Correction du 'loyer_mensuel' négatif
    negative_loyer = df[df['loyer_mensuel'] < 0]['loyer_mensuel'].count()
    if negative_loyer > 0:
        print(f"Correction de {negative_loyer} valeur(s) de 'loyer_mensuel' négatives en les passant en valeur absolue.")
        df['loyer_mensuel'] = df['loyer_mensuel'].abs()

    # Clipping des outliers pour 'montant_pret' et 'revenu_estime_mois'
    for col in ['montant_pret', 'revenu_estime_mois']:
        if col in df.columns:
            q99 = df[col].quantile(0.99)
            outliers_count = df[df[col] > q99][col].count()
            if outliers_count > 0:
                print(f"Clipping de {outliers_count} outliers pour '{col}' à la valeur du 99ème percentile ({q99:.2f}).")
                df[col] = np.where(df[col] > q99, q99, df[col])

    # --- 4. Imputer les valeurs NULL/NaN ---
    print("\n--- Étape 4: Imputation des valeurs manquantes ---")
    numerical_cols = df.select_dtypes(include=np.number).columns
    
    for col in numerical_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            print(f"Imputation des valeurs manquantes dans '{col}' avec la médiane ({median_val:.2f}).")
            df[col].fillna(median_val, inplace=True)
            
    print("\nVérification des valeurs manquantes après imputation:\n", df.isnull().sum())

    # --- Sauvegarde ---
    print(f"\nSauvegarde des données nettoyées dans {output_file}...")
    df.to_csv(output_file, index=False)
    print("Nettoyage terminé. Shape final:", df.shape)

if __name__ == '__main__':
    clean_data()
