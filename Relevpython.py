import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Code HTML et CSS intégré
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        rel="stylesheet"
    >
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 20px;
        }
    </style>
    <title>Streamlit with Bootstrap</title>
</head>
<body>
    <div class="container">
        <div class="jumbotron mt-4">
            <h1 class="display-4">Hello, Streamlit!</h1>
            <p class="lead">This is a simple integration of Bootstrap with Streamlit.</p>
            <hr class="my-4">
            <p>Use Bootstrap components to enhance your Streamlit app.</p>
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </div>
    </div>
</body>
</html>
"""

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
