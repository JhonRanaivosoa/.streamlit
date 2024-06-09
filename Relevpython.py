import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Définir la configuration de la page pour activer le mode large
st.set_page_config(layout="wide")


# Afficher le contenu HTML dans Streamlit
st.markdown(html_template, unsafe_allow_html=True)

# Ajoutez votre propre contenu Streamlit
st.title("Streamlit Application with Bootstrap")
st.write("This is a sample application using Streamlit and Bootstrap for styling.")

# Exemple de graphique avec Plotly
# Générer des données aléatoires pour l'exemple
df = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

# Créer une figure Plotly
fig = px.line(df, x='a', y='b', title='Random Data Line Chart')

# Afficher la figure Plotly dans Streamlit
st.plotly_chart(fig)
