import streamlit as st
import gdown
import pandas as pd

# Lien partagé du fichier sur Google Drive
url = 'https://drive.google.com/file/d/1ntNnU53yyZg9V5Gt-wwctEIoMLX3c-L-/view?usp=drive_link'

# Télécharger le fichier dans un répertoire temporaire
output = 'file.csv'  # Nom du fichier de sortie

with st.spinner('Téléchargement du fichier...'):
    gdown.download(url, output, quiet=False)

st.success('Fichier téléchargé avec succès !')

# Charger et afficher le contenu du fichier
st.write("Contenu du fichier :")
df = pd.read_csv(output)
st.write(df)

