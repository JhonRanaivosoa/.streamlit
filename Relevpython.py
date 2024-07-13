
import streamlit as st
import pandas as pd
import plotly.express as px

# Créer un jeu de données simple
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [150, 200, 250, 300, 350, 400]
}
df = pd.DataFrame(data)

# Titre de l'application
st.title("Tableau de Bord des Ventes Mensuelles")

# Affichage du jeu de données sous forme de tableau
st.header("Jeu de Données")
st.table(df)

# Commande pour filtrer les données par mois
selected_months = st.multiselect(
    'Sélectionnez les Mois à Afficher',
    options=df['Month'].unique(),
    default=df['Month'].unique()
)

# Filtrer les données en fonction des mois sélectionnés
filtered_df = df[df['Month'].isin(selected_months)]

# Affichage du graphique des ventes
st.header("Graphique des Ventes Mensuelles")
fig = px.bar(filtered_df, x='Month', y='Sales', title='Ventes Mensuelles')
st.plotly_chart(fig)
