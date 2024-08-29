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
data = load_data(excel_url, "BMOI SANIFER")

st.title("GROUP TALYS")

st.title("SANIFER BMOI")

st.write(data)

import streamlit as st

# Ajouter un titre dans la barre latérale
st.sidebar.title("Navigation")

# Ajouter des options de navigation dans la barre latérale
option = st.sidebar.selectbox(
    "Choisissez une page",
    ("Accueil", "Analyse", "Rapports", "Contact")
)

# Afficher le contenu en fonction de la sélection
if option == "Accueil":
    st.title("Bienvenue à la page d'accueil")
    st.write("Ceci est la page d'accueil.")

elif option == "Analyse":
    st.title("Page d'analyse")
    st.write("Ceci est la page d'analyse.")

elif option == "Rapports":
    st.title("Page des rapports")
    st.write("Ceci est la page des rapports.")

elif option == "Contact":
    st.title("Page de contact")
    st.write("Ceci est la page de contact.")




