import csv
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('f4x.db')
cursor = conn.cursor()

# Ejecutar la consulta SQL
cursor.execute("SELECT * FROM Games")

# Obtener los resultados de la consulta
results = cursor.fetchall()

# Especificar el nombre del archivo de salida
nombre_archivo = 'games.txt'

# Exportar los resultados a un archivo CSV
with open(nombre_archivo, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(results)

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()
