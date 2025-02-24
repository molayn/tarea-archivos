import pandas as pd
file_path = "C:/Users/juank/Documents/PROGRAMACION/Trabajo/SalesJan2009.csv"  
df = pd.read_csv(file_path)


medio_pago = input("Ingrese el medio de pago: ").strip()
compras_pago = df[df['Payment_Type'].str.strip().str.lower() == medio_pago.lower()]


total_compras = len(compras_pago)


print(f"Total de compras con {medio_pago}: {total_compras}")