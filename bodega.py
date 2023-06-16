from typing import ItemsView


ac = {"1100": 4, "V3": 2, "V8": 1, "Belkin V8": 10, "Belkin TC": 10, "6101": 3}
cb = {"WW TC caja": 5, "Batri V8 Bolsa ": 5}
fd = {}
ml = {"B10 Negro": 2, "Bolsa Blanco": 5, "Bolsa negro ": 5, "S6 Blanco": 5, "AKG": 5}
sl = {
    "Note 11 Rojo": 1,
    "Redmi 10 Verde militar": 1,
    "S10 Plus Negro": 1,
    "J6 Plus Negro": 2,
    "A02s Gris": 2,
    "Moto E20 Rojo": 1,
}

glosario = {
    "ac": "cargadores",
    "ml": "manos libres",
    "sl": "Silicone Case",
    "fd": "Forro Diseños",
}

seleccion = input(f"Ver listado de productos 1- Si 2-No")
if seleccion == "1":
    print(glosario)
else:
    producto = input("consultar...")
    if producto == "ac":
        print("_" * 40)
        for x, y in ac.items():
            print(f"Cargador {x} = {y}")
    if producto == "cb":
        print("_" * 40)
        for x, y in cb.items():
            print(f"Cable {x} = {y}")
    if producto == "fd":
        print("_" * 40)
        for x, y in fd.items():
            print(f"Forro Diseños {x} = {y}")
    if producto == "ml":
        print("_" * 40)
        for x, y in ml.items():
            print(f"Manos Libres {x} = {y}")
    if producto == "sl":
        print("_" * 40)
        for x, y in sl.items():
            print(f"Silicone Case {x} = {y}")
    else:
        print("No encontrado")
