import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
data = load_data(excel_url, "MCB SANIFER")

# Vérifier si les données ont été chargées
if data is not None:
    # Extraire la colonne 'Solde courant'
    if 'Solde courant' in data.columns:
        # Convertir la colonne en numérique, forcer les erreurs à NaN
        data['Solde courant'] = pd.to_numeric(data['Solde courant'], errors='coerce')
        
        # Supprimer les valeurs manquantes
        solde = data['Solde courant'].dropna()
        
        # Créer le graphique
        fig, ax = plt.subplots()

        # Créer des segments pour les couleurs conditionnelles
        ax.plot(solde.index, solde, color='grey', alpha=0.5, label='Solde courant')  # Tracer la courbe en gris de base

        # Colorier les parties en dessous de 0 en rouge
        below_zero = solde[solde < 0]
        ax.fill_between(below_zero.index, below_zero, color='red', alpha=0.5, label='En dessous de 0')

        # Colorier les parties au-dessus de 0 en bleu
        above_zero = solde[solde >= 0]
        ax.fill_between(above_zero.index, above_zero, color='blue', alpha=0.5, label='Au-dessus de 0')

        # Ajouter des labels et une légende
        ax.set_title('Évolution de la colonne Solde courant')
        ax.set_xlabel('Index')
        ax.set_ylabel('Solde courant')
        ax.legend()

        # Afficher le graphique dans Streamlit
        st.pyplot(fig)
    else:
        st.write("La colonne 'Solde courant' n'existe pas dans la feuille.")
else:
    st.write("Les données n'ont pas pu être chargées.")
