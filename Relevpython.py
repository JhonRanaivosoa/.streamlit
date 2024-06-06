


import streamlit as st
import pandas as pd
from mega import Mega

# Se connecter à MEGA
mega = Mega()
email = 'jhonranaivosoa@gmail.com'
password = 'Harisoa5janvier1998.'
m = mega.login(email, password)

# Télécharger le fichier depuis MEGA
file = m.download_url('https://mega.nz/file/jegUxbiZ#qC8qz9q_PcH4OUBUKImXJ6fy6BI-YKt6rJawTWk-FC8')

# Lire le fichier téléchargé (en supposant qu'il s'agit d'un fichier CSV)
data = pd.read_csv(file)

# Afficher les données sur Streamlit
st.title('Données téléchargées de MEGA')
st.dataframe(data)
