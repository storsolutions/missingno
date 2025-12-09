
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('fichier-de-donnees-numeriques-69202f25dea8b267811864.csv')

# 1. Descriptive Statistics
print("Statistiques descriptives du DataFrame:")
print(df.describe().to_markdown())

# 2. Outlier Detection using Boxplots
numerical_cols = df.select_dtypes(include=['number']).columns

for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot de {col}', fontsize=16)
    plt.ylabel(col, fontsize=12)
    plt.savefig(f'boxplot_{col}.png')
    plt.close()
    print(f"Boxplot pour {col} enregistré sous 'boxplot_{col}.png'")
