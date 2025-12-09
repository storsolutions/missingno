
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('fichier-de-donnees-numeriques-69202f25dea8b267811864.csv')

# 1. Histograms and Density Plots for each numerical feature
numerical_cols = df.select_dtypes(include=['number']).columns

for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution de {col} (Histogramme et Densité)', fontsize=16)
    plt.xlabel(col, fontsize=12)
    plt.ylabel('Fréquence / Densité', fontsize=12)
    plt.savefig(f'distribution_{col}.png')
    plt.close()
    print(f"Distribution pour {col} enregistrée sous 'distribution_{col}.png'")

# 2. Pairplot to visualize relationships between numerical features
# Due to the large number of features and potential for long execution,
# we might consider sampling or selecting a subset of features for pairplot if needed.
# For now, let's try with all numerical columns.
print("\nGénération du Pairplot (cela peut prendre du temps pour de nombreuses colonnes)...")
sns_plot = sns.pairplot(df.select_dtypes(include=['number']).dropna())
sns_plot.fig.suptitle('Pairplot des Caractéristiques Numériques', y=1.02, fontsize=16)
sns_plot.savefig('pairplot_numerical_features.png')
print("Pairplot enregistré sous 'pairplot_numerical_features.png'")
plt.close()
