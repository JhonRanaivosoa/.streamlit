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
    # Afficher les premières lignes de la feuille pour vérification
    st.write("Données de la feuille 'MCB SANIFER':")
    st.write(data.head())

    # Vérifier si les colonnes nécessaires existent
    if 'Solde courant' in data.columns and 'Date d\'opération' in data.columns:
        # Convertir la colonne 'Date d\'opération' en datetime
        data['Date d\'opération'] = pd.to_datetime(data['Date d\'opération'], errors='coerce')
        
        # Convertir la colonne 'Solde courant' en numérique, forcer les erreurs à NaN
        data['Solde courant'] = pd.to_numeric(data['Solde courant'], errors='coerce')
        
        # Supprimer les lignes avec des valeurs manquantes dans les deux colonnes
        data = data.dropna(subset=['Date d\'opération', 'Solde courant'])
        
        # Créer le graphique avec Plotly
        fig = go.Figure()

        # Ajouter la trace pour la colonne 'Solde courant'
        fig.add_trace(go.Scatter(
            x=data['Date d\'opération'],
            y=data['Solde courant'],
            mode='lines',
            line=dict(color='blue'),
            name='Solde courant'
        ))

        # Mettre en forme le graphique
        fig.update_layout(
            title='Évolution de la colonne Solde courant',
            xaxis_title='Date d\'opération',
            yaxis_title='Solde courant',
            showlegend=True
        )

        # Afficher le graphique dans Streamlit
        st.plotly_chart(fig)
    else:
        st.write("Les colonnes 'Solde courant' ou 'Date d\'opération' n'existent pas dans la feuille.")
else:
    st.write("Les données n'ont pas pu être chargées.")

