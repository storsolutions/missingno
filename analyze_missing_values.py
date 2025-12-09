
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('fichier-de-donnees-numeriques-69202f25dea8b267811864.csv')

# 1. Nullity Matrix
plt.figure(figsize=(12, 8))
msno.matrix(df, figsize=(12, 8), sparkline=False, fontsize=10, labels=True)
plt.title('Matrice de Nullité', fontsize=16)
plt.savefig('nullity_matrix.png')
print("Matrice de nullité enregistrée sous 'nullity_matrix.png'")
plt.close()

# 2. Bar Chart of Nullity
plt.figure(figsize=(12, 6))
msno.bar(df, figsize=(12, 6), fontsize=10, color='steelblue')
plt.title('Graphique à Barres des Valeurs Manquantes', fontsize=16)
plt.savefig('nullity_bar_chart.png')
print("Graphique à barres des valeurs manquantes enregistré sous 'nullity_bar_chart.png'")
plt.close()

# 3. Heatmap of Nullity Correlation
plt.figure(figsize=(10, 8))
msno.heatmap(df, figsize=(10, 8), fontsize=10)
plt.title('Heatmap de Corrélation des Valeurs Manquantes', fontsize=16)
plt.savefig('nullity_heatmap.png')
print("Heatmap de corrélation des valeurs manquantes enregistrée sous 'nullity_heatmap.png'")
plt.close()
