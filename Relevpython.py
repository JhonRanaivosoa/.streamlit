import streamlit as st

def main():
    st.title('Exemple Streamlit avec HTML et Bootstrap')

    # Lecture du fichier HTML
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Affichage du contenu HTML
     st.write(html_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
