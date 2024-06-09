import streamlit as st
import requests
import pandas as pd


# Charger et afficher le contenu du fichier
st.write("Contenu du fichier :")
df = pd.read_csv(output)
st.write(df)
