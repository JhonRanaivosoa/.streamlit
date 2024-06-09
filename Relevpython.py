


import streamlit as st
import pandas as pd
from mega import Mega

# Se connecter à MEGA
mega = Mega()
email = 'jhonranaivosoa@gmail.com'
password = 'Harisoa5janvier1998.'
m = mega.login(email, password)

# Télécharger le fichier depuis MEGA
file_link = 'https://mega.nz/file/jegUxbiZ#qC8qz9q_PcH4OUBUKImXJ6fy6BI-YKt6rJawTWk-FC8'
file_name = '00811820101_1717050720642.csv'  # Nom sous lequel vous souhaitez sauvegarder le fichier localement
m.download_url(file_link, file_name)

# Lire le fichier téléchargé (en supposant qu'il s'agit d'un fichier CSV)
df = pd.read_csv(file_name)

# Afficher les données sur Streamlit
st.title('Données téléchargées de MEGA')
st.dataframe(df)
