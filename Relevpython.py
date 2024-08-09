import streamlit as st
import pandas as pd

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
        solde = data[['Solde courant']]  # Extraire uniquement la colonne 'Solde courant'
        
        # Afficher la colonne dans Streamlit
        st.write("Données de la colonne 'Solde courant' :")
        st.dataframe(solde)
    else:
        st.write("La colonne 'Solde courant' n'existe pas dans la feuille.")
else:
    st.write("Les données n'ont pas pu être chargées.")

