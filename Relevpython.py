import streamlit as st
import requests
import pandas as pd

# Lien partagé du fichier sur Google Drive
file_id = 'YOUR_FILE_ID'
url = f'https://drive.google.com/uc?id={file_id}'

# Fonction pour télécharger le fichier depuis Google Drive
def download_file_from_google_drive(url, output):
    session = requests.Session()
    response = session.get(url, stream=True)
    token = None

    for key, value in session.cookies.items():
        if key.startswith('download_warning'):
            token = value

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    with open(output, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Télécharger le fichier dans un répertoire temporaire
output = 'file.csv'  # Nom du fichier de sortie

with st.spinner('Téléchargement du fichier...'):
    download_file_from_google_drive(url, output)

st.success('Fichier téléchargé avec succès !')

# Charger et afficher le contenu du fichier
st.write("Contenu du fichier :")
df = pd.read_csv(output)
st.write(df)
