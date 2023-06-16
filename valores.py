process = int(input("Select process 1-Recargas 2-Iva: 3-Bancos 4-Cobros:  "))
import pyperclip

bancolombia = {171122: 256128, 181122: 436128}
nequi = {171122: 198964, 181122: 178964}
daviplata = {171122: 307633, 181122: 307633}
recargas = {171122: 54763, 181122: 68264}
disney = {"Migdalia": "01 de cada mes", "Yineth": "19 de cada mes"}
if process == 1:
    sell = int(input("Valor de la venta: "))
    prc = (7 / 100) + 1
    vlbs = sell / prc
    gnc = sell - vlbs
    print("Selecciono Recargas")
    print(f"Venta: {sell}")
    print(f"Inversion: {round (vlbs,2)} (valor base)")
    print("Utilidad 7%")
    print(f"Ganancia: {round (gnc,2)}")
    vlscopy = round(vlbs)-1
    pyperclip.copy(vlscopy)
elif process == 2:
    sell = int(input("Valor de la venta: "))
    iva = "19%"
    vlbs = sell / 1.19
    print(f"Selecciono IVA x venta {sell}")
    print(f"Precio antes de iva: {round (vlbs,2)}")
    print(f"IVA: {round(sell - vlbs,2)} (19%)")
    print(f"Total: {sell}")
elif process == 3:
    date = int(input("fecha que desea consultar?: "))
    print(f"""=======infobank {date}=======""")
    print(f"Bancolombia: {bancolombia[date]}")
    print(f"Nequi: {nequi[date]}")
    print(f"DaviPlata: {daviplata[date]}")
    print(f"Recargas: {recargas[date]}")
    print(
        f"Total: {int(bancolombia[date])+int(nequi[date])+int(daviplata[date])+int(recargas[date])}"
    )
elif process == 4:
    claves = disney.keys()
    print(f"Listado de clientes {claves}")
    cliente = input("digite el nombre del cliente... ")
    print(f"El {disney[cliente]}")
else:
    print("Operacion no encontrada o valor no valido intente nuevamente ...")
    process = int(input("Select process 1-Recargas 2-Iva: 3-Bancos :"))
