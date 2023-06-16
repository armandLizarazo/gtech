import pickle

with open("datos.pkl", "rb") as archivo:
    datos = pickle.load(archivo)

item1 = 1
marca = input("Marca")
ref = input("referencia")
datos = [marca, ref ]
datos.extend(datos)

with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

print(datos)
