
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_data_before_after(original_file='fichier-de-donnees-numeriques-69202f25dea8b267811864.csv', cleaned_file='donnees_nettoyees.csv'):
    """
    This script performs a statistical analysis of the original and cleaned datasets,
    comparing their descriptive statistics and distributions.
    """
    print(f"Chargement des données originales depuis {original_file}...")
    df_original = pd.read_csv(original_file)
    print("Données originales chargées. Shape:", df_original.shape)

    print(f"\nChargement des données nettoyées depuis {cleaned_file}...")
    df_cleaned = pd.read_csv(cleaned_file)
    print("Données nettoyées chargées. Shape:", df_cleaned.shape)

    # --- 1. Statistiques descriptives avant/après ---
    print("\n--- Statistiques descriptives - DONNÉES ORIGINALES ---")
    print(df_original.describe().to_markdown())

    print("\n--- Statistiques descriptives - DONNÉES NETTOYÉES ---")
    print(df_cleaned.describe().to_markdown())

    # --- 2. Comparaison visuelle des distributions ---
    print("\n--- Comparaison visuelle des distributions (histograms/density plots) ---")
    
    # Identify common numerical columns for comparison
    numerical_cols_original = df_original.select_dtypes(include=np.number).columns
    numerical_cols_cleaned = df_cleaned.select_dtypes(include=np.number).columns
    
    # Only compare columns that exist in both (cleaned might have fewer columns)
    common_numerical_cols = list(set(numerical_cols_original) & set(numerical_cols_cleaned))
    
    for col in common_numerical_cols:
        plt.figure(figsize=(14, 6))
        
        # Original data
        plt.subplot(1, 2, 1)
        sns.histplot(df_original[col].dropna(), kde=True, color='skyblue')
        plt.title(f'Original - Distribution de {col}', fontsize=14)
        plt.xlabel(col, fontsize=12)
        plt.ylabel('Fréquence / Densité', fontsize=12)
        
        # Cleaned data
        plt.subplot(1, 2, 2)
        sns.histplot(df_cleaned[col].dropna(), kde=True, color='lightcoral')
        plt.title(f'Nettoyé - Distribution de {col}', fontsize=14)
        plt.xlabel(col, fontsize=12)
        plt.ylabel('Fréquence / Densité', fontsize=12)
        
        plt.tight_layout()
        plt.savefig(f'distribution_comparison_{col}.png')
        plt.close()
        print(f"Comparaison de distribution pour '{col}' enregistrée sous 'distribution_comparison_{col}.png'")

    print("\nAnalyse statistique avant/après terminée.")

if __name__ == '__main__':
    analyze_data_before_after()
