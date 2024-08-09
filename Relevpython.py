import pandas as pd
import plotly.express as px

# Exemple de données
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 12, 67, 34]
}

# Conversion des données en DataFrame
df = pd.DataFrame(data)

# Calculs de base
somme = df['Values'].sum()
moyenne = df['Values'].mean()

print(f"Somme des valeurs : {somme}")
print(f"Moyenne des valeurs : {moyenne}")

# Création d'un graphique en barres
fig = px.bar(df, x='Category', y='Values', title='Graphique des valeurs par catégorie')

# Affichage du graphique
fig.show()
