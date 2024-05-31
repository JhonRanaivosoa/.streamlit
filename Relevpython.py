


import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Visualisation de données")

# Charger les données
data = pd.read_csv('data.csv')

# Afficher les données
st.write(data)

# Créer un graphique
st.line_chart(data)
