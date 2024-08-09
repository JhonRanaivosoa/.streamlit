import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# URL brute du fichier Excel sur GitHub
excel_url = "https://raw.githubusercontent.com/JhonRanaivosoa/streamlittest/5d21b841763b7f5e76e4e2ffbebc35193d81248a/RELEVE%20SANIFER%202024.xlsx"

# Fonction pour charger les données de la feuille spécifiée
@st.cache
def load_data(url, sheet_name):
    try:
        return pd.read_excel(url, sheet_name=sheet_name)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

# Charger les données de la feuille "MCB SANIFER"
data = load_data(excel_url, "MCB SANIFER")

# Vérifier si les données ont été chargées
if data is not None:
    # Extraire la colonne 'Solde courant'
    if 'Solde courant' in data.columns:
        # Convertir la colonne en numérique, forcer les erreurs à NaN
        data['Solde courant'] = pd.to_numeric(data['Solde courant'], errors='coerce')
        
        # Supprimer les valeurs manquantes
        solde = data['Solde courant'].dropna()
        
        # Créer le graphique avec Plotly
        fig = go.Figure()

        # Ajouter la trace pour les valeurs en dessous de 0
        below_zero = solde[solde < 0]
        fig.add_trace(go.Scatter(
            x=below_zero.index,
            y=below_zero,
            mode='lines',
            line=dict(color='red'),
            name='En dessous de 0'
        ))

        # Ajouter la trace pour les valeurs au-dessus de 0
        above_zero = solde[solde >= 0]
        fig.add_trace(go.Scatter(
            x=above_zero.index,
            y=above_zero,
            mode='lines',
            line=dict(color='blue'),
            name='Au-dessus de 0'
        ))

        # Mettre en forme le graphique
        fig.update_layout(
            title='Évolution de la colonne Solde courant',
            xaxis_title='Index',
            yaxis_title='Solde courant',
            showlegend=True
        )

        # Afficher le graphique dans Streamlit
        st.plotly_chart(fig)
    else:
        st.write("La colonne 'Solde courant' n'existe pas dans la feuille.")
else:
    st.write("Les données n'ont pas pu être chargées.")
