import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Définir la configuration de la page pour activer le mode large
st.set_page_config(layout="wide")

# Ajouter du JavaScript pour recharger la page toutes les 30 secondes
st.markdown(
    """
    <script>
    function reload() {
        setTimeout(function() {
            window.location.reload(1);
        }, 30000); // 30000 milliseconds = 30 seconds
    }
    window.onload = reload;
    </script>
    """,
    unsafe_allow_html=True
)

# Code HTML et CSS intégré avec une navbar Bootstrap
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
        .navbar-custom {
            background: linear-gradient(90deg, rgba(255,0,0,0.08), rgba(255,165,0,0.08), rgba(238,130,238,0.08), rgba(0,0,255,0.08));
            position: fixed;
            width: 100%;
            z-index: 1000;
        }
        .content {
            margin-top: 70px; /* Ajouter une marge supérieure pour éviter que le contenu ne soit caché derrière la navbar */
        }
    </style>
    <title>Streamlit with Bootstrap</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light navbar-custom">
        <a class="navbar-brand" href="#">Streamlit App</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container content">
        <div class="jumbotron mt-4">
            <h1 class="display-4">Hello, Streamlit!</h1>
            <p class="lead">This is a simple integration of Bootstrap with Streamlit.</p>
            <hr class="my-4">
            <p>Use Bootstrap components to enhance your Streamlit app.</p>
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvvh59yXyy5fw20y" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa5mGVmJC7MGg1MD11RKs4p8" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-a5fw8p5PdcA0P3McN8z2Wm2f8QbKwlG5BO1Z8rJ3tnv8e5xQOltH4l90ph7PtFi" crossorigin="anonymous"></script>
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
