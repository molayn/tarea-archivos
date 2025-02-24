import pandas as pd

file_path = "C:/Users/juank/Documents/PROGRAMACION/Trabajo/SalesJan2009.csv" #
df = pd.read_csv(file_path)

pais = input("Ingrese el país: ").strip()  
compras_pais = df[df['Country'].str.strip().str.lower() == pais.lower()]



total_compras = len(compras_pais)


print(f"Total de compras en {pais}: {total_compras}")



