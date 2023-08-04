import locale
from mimetypes import init
import pyperclip
import datetime 
import locale
import calendar

hora_actual = datetime.datetime.now().time()
dia_actual = datetime.datetime.now()
date_format = hora_actual.strftime("%I:%M:%S")
fecha_actual = datetime.datetime.now()
ahora_d = calendar.day_name[fecha_actual.weekday()]
ahora_dn = fecha_actual.strftime('%d')
ahora_m = calendar.month_name[fecha_actual.month]
ahora_y = fecha_actual.strftime("%Y")
init = int(input("1 para calcular o 0 para salir:"))



if init != [0, 1]:
    while init == 1:
        sell = int(input("valor de la venta:"))
        sold = sell
        prc = (7 / 100) + 1
        vlbs = sell / prc
        gnc = sell - vlbs
        line = "=" * 20
        print(line)
        print(f"Venta: {sell}")
        print(f"Inversion: {round (vlbs,2)} (valor base)")
        print("Utilidad 7%")
        print(f"Ganancia: {round (gnc,2)}")
        print(f"{ahora_d} {ahora_dn} {ahora_m} {ahora_y} {date_format}")
        vlscopy = round(vlbs)-1
        gnccopy = round(gnc,2)
        pyperclip.copy(vlscopy)
        parar = input("pulsa 'e' para salir o cualquier otra tecla para continuar...")
        if parar == "e":
            print("...finalizado!!")
            print(date_format)
            break
    else:
        print("Opcion no valida")
        print(hora_actual)
