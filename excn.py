import pandas as pd

df = pd.read_excel("controlMercancia.xlsx")

# Filtrar los datos según una condición
df_filtrado = df[df["Categoria"] == "Pacha"]

# Escribir los datos filtrados a otro archivo de Excel
df_filtrado.to_excel("resultado.xlsx")
