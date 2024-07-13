
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
# Ajouter le CSS de Bootstrap
st.markdown("""
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f0f2f6;
        }
        .navbar {
            margin-bottom: 20px;
        }
        .card {
            background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(0,212,255,1) 100%);
            color: white;
        }
        .btn-primary {
            background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Créer une barre de navigation
st.markdown("""
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Tableau de Bord</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Accueil <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Données</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Analyse</a>
                </li>
            </ul>
        </div>
    </nav>
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

# Ajouter un bouton Bootstrap pour réinitialiser la sélection
if st.button('Réinitialiser la Sélection', key="reset", css_classes="btn btn-primary"):
    st.experimental_rerun()
