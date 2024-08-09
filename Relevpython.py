import streamlit as st
import pandas as pd
import plotly.express as px



# Titre de l'application
st.title("Calculs et Visualisation avec Plotly")

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

# Affichage des résultats des calculs
st.write(f"**Somme des valeurs** : {somme}")
st.write(f"**Moyenne des valeurs** : {moyenne}")

# Création d'un graphique en barres
fig = px.bar(df, x='Category', y='Values', title='Graphique des valeurs par catégorie')

# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
