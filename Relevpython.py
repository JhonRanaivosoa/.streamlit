
import streamlit as st
import pandas as pd
import plotly.express as px

# CSS personnalisé pour le style
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);
        color: white;
    }
    .stMetric {
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(0,212,255,1) 100%);
        color: white;
    }
    .css-1kyxreq {
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(0,212,255,1) 100%);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Titre de l'application
st.title("Tableau de Bord Interactif des Ventes Mensuelles")

# Créer un jeu de données simple
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [150, 200, 250, 300, 350, 400]
}
df = pd.DataFrame(data)

# Commande pour filtrer les données par mois
selected_months = st.multiselect(
    'Sélectionnez les Mois à Afficher',
    options=df['Month'].unique(),
    default=df['Month'].unique()
)

# Filtrer les données en fonction des mois sélectionnés
filtered_df = df[df['Month'].isin(selected_months)]

# Section avec des métriques clés
st.header("Métriques Clés")
total_sales = filtered_df['Sales'].sum()
average_sales = filtered_df['Sales'].mean()
st.metric(label="Ventes Totales", value=f"{total_sales} USD")
st.metric(label="Vente Moyenne", value=f"{average_sales:.2f} USD")

# Affichage du graphique des ventes
st.header("Graphique des Ventes Mensuelles")
fig = px.bar(filtered_df, x='Month', y='Sales', title='Ventes Mensuelles', color='Sales',
             color_continuous_scale='Bluered', template='plotly_dark')
fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
st.plotly_chart(fig)

# Affichage des données filtrées sous forme de tableau
st.header("Données Filtrées")
st.table(filtered_df)

# Ajout d'un bouton pour réinitialiser la sélection
if st.button('Réinitialiser la Sélection'):
    st.experimental_rerun()
