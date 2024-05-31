


import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Visualisation de données")

# Charger les données
data = [1,2,3,4,5,6]

# Afficher les données
st.write(data)

# Créer un graphique
st.line_chart(data)
