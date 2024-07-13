import streamlit as st
import pandas as pd

# URL de téléchargement direct de Google Drive
csv_url = 'https://drive.google.com/file/d/1ntNnU53yyZg9V5Gt-wwctEIoMLX3c-L-/view?usp=drive_link'

# Lire le fichier CSV depuis Google Drive
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(csv_url)

# Afficher les données dans Streamlit
st.write(data)
