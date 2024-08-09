import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import hydralit_components as hc

menu_data = [
    {'label':"Left End"},
    {'label':"Book"},
    {'label':"Component"},
    {'label':"Dashboard"},
    {'label':"Right End"},
]

menu_id = hc.nav_bar(menu_definition=menu_data)

st.info(f"{menu_id=}")
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




