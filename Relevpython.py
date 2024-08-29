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

st.title("SANIFER BMOI")

st.write(data)

import streamlit as st

# Ajouter un titre dans la barre latérale
st.sidebar.title("Navigation")

# Ajouter des options de navigation dans la barre latérale
option = st.sidebar.selectbox(
    "Choisissez une page",
    ("Accueil", "Analyse", "Rapports", "Contact")
)

# Afficher le contenu en fonction de la sélection
if option == "Accueil":
    st.title("Bienvenue à la page d'accueil")
    st.write("Ceci est la page d'accueil.")

elif option == "Analyse":
    st.title("Page d'analyse")
    st.write("Ceci est la page d'analyse.")

elif option == "Rapports":
    st.title("Page des rapports")
    st.write("Ceci est la page des rapports.")

elif option == "Contact":
    st.title("Page de contact")
    st.write("Ceci est la page de contact.")

import streamlit as st
from fpdf import FPDF

# Fonction pour générer le PDF
def generate_pdf(beneficiary, amount, reference, bank_details):
    pdf = FPDF()
    pdf.add_page()

    # Titre
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Ordre de Virement", ln=True, align="C")

    # Détails du virement
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Bénéficiaire: {beneficiary}", ln=True)
    pdf.cell(200, 10, txt=f"Montant: {amount} EUR", ln=True)
    pdf.cell(200, 10, txt=f"Référence: {reference}", ln=True)
    pdf.cell(200, 10, txt=f"Détails bancaires: {bank_details}", ln=True)

    return pdf.output(dest="S").encode("latin1")

# Interface Streamlit
st.title("Création d'un Ordre de Virement")

beneficiary = st.text_input("Nom du Bénéficiaire")
amount = st.text_input("Montant (EUR)")
reference = st.text_input("Référence")
bank_details = st.text_area("Détails bancaires")

if st.button("Générer le PDF"):
    if beneficiary and amount and reference and bank_details:
        pdf_content = generate_pdf(beneficiary, amount, reference, bank_details)
        st.download_button(
            label="Télécharger l'Ordre de Virement en PDF",
            data=pdf_content,
            file_name="ordre_de_virement.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("Veuillez remplir tous les champs du formulaire.")




