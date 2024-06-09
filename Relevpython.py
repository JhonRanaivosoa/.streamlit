
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Créer un tableau de données aléatoires
np.random.seed(42)  # Pour la reproductibilité des résultats
data = {
    'X': np.random.rand(100),
    'Y': np.random.rand(100)
}
df = pd.DataFrame(data)

# Afficher les premières lignes du tableau
st.write("Tableau des Données Aléatoires")
st.write(df.head())

# Créer un graphique en nuage de points avec Plotly Express
fig = px.scatter(df, x='X', y='Y', title='Scatter Plot des Données Aléatoires')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)
