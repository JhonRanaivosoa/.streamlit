


#IMPORTATION BIBLIOTHEQUES
import pandas as pd 
import time
import numpy as np
import plotly.express as px 
import streamlit as st 
import os
from mega import Mega
import io


#Définition lien
import asyncio
async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine exécutée")

async def main():
    await my_coroutine()
asyncio.run(main())

# Se connecter à MEGA
mega = Mega()
email = 'jhonranaivosoa@gmail.com'
password = 'Harisoa5janvier1998.'
m = mega.login(email, password)

# Chemin du fichier à téléverser
file_path = r'C:\Users\Tahinjanahary Jhon\Desktop\Data base\Relever transaction\releve.csv'

# Téléverser le fichier
file = m.upload(file_path)

# Obtenir le lien du fichier téléversé
link = m.get_upload_link(file)
print("Fichier téléversé avec succès ! Lien : {link}")
