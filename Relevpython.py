import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# URL brute du fichier Excel sur GitHub
excel_url = "https://raw.githubusercontent.com/JhonRanaivosoa/streamlittest/5d21b841763b7f5e76e4e2ffbebc35193d81248a/RELEVE%20SANIFER%202024.xlsx"

# Fonction pour charger les données de la feuille spécifiée
@st.cache
def load_data(url, sheet_name):
    try:
        return pd.read_excel(url, sheet_name=sheet_name)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None

# Charger les données de la feuille "MCB SANIFER"
data = load_data(excel_url, "BMOI SANIFER")

st.title("GROUP TALYS")

st.titl("SANIFER BMOI")

st.write(data)


import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Exemple de données en milliards
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='M'),
    'Valeur': [1.2, 0.5, -0.3, 2.4, -1.0, 1.8, 0.9, -0.2, 0.4, 1.1]  # Données en milliards
}

df = pd.DataFrame(data)

# Créer une trace avec Plotly
fig = go.Figure()

# Ajouter une trace pour les valeurs supérieures ou égales à 0 (en bleu)
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Valeur'].where(df['Valeur'] >= 0, None),
    mode='lines',
    line=dict(color='blue'),
    name='Valeurs >= 0'
))

# Ajouter une trace pour les valeurs inférieures à 0 (en rouge)
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Valeur'].where(df['Valeur'] < 0, None),
    mode='lines',
    line=dict(color='red'),
    name='Valeurs < 0'
))

# Configurer la mise en page du graphique
fig.update_layout(
    title='Courbe Graphique des Valeurs en Milliards',
    xaxis_title='Date',
    yaxis_title='Valeur (en milliards)',
    template='plotly_white'
)

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)
