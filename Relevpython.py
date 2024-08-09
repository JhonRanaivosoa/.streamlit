import streamlit as st
import pandas as pd

# URL du fichier Excel sur GitHub
excel_url = "https://raw.githubusercontent.com/votre-utilisateur/votre-repo/main/RELEVE%20SANIFER%202024/RELEVE%20SANIFER%202024.xlsx"

# Fonction pour charger les données du fichier Excel
@st.cache
def load_data(url):
    return pd.read_excel(url, sheet_name=None)  # `sheet_name=None` charge toutes les feuilles

# Charger les données
data = load_data(excel_url)

# Afficher les noms des feuilles dans l'application Streamlit
st.title("Données du fichier Excel")
st.write("Feuilles disponibles :")
for sheet_name in data.keys():
    st.write(f"- {sheet_name}")

# Afficher les données de la première feuille
first_sheet = list(data.keys())[0]
st.write(f"**Données de la feuille : {first_sheet}**")
st.write(data[first_sheet])
