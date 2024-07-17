import pandas as pd

# Remplacer 'votre_fichier.csv' par le nom de votre fichier CSV
file_path = 'C:\Users\jhon.treso\OneDrive - Sanifer\Bureau\15\00811820101_1721109524739.csv'

# Lire le fichier CSV
df = pd.read_csv(file_path)

# Afficher le contenu du fichier CSV
print(df)
