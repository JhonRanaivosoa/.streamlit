import streamlit as st

def main():
    st.title('Exemple Streamlit avec HTML et Bootstrap')

    # Lecture du fichier HTML
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Affichage du contenu HTML
     st.components.v1.html(html_content, height=600, scrolling=True

if __name__ == '__main__':
    main()
