from pickle import APPEND
from webbrowser import get

prov = {
  "pacha zte ": "Cs,120 Cl,160",
  "numero claro": "*611# llamar y seguir los pasos",
  "numero movistar": "*611# llamar",
  "numero tigo": "*255*4# llamar",
  "numero wom": "*302 llamar y seguir los pasos",
  "numero virgin": "*111# llamar y seguir los pasos",
  "numero flash mobile": "+555 llamar",
  "valuntech 60": 1,
  "sebastian": 2,
  "smart plus": 3,
  "rubiani": 4,
  "joma": 5,
  "ovidio": 6,
  "atraspr": 7,
  "pr95": 8,
  "controles": 9,
  "el huracan": 10,
  "el surtidor": 11,
  "batri mundotech": 12,
  "vj": 13,
  "yolima tecno one": 14,
  "wom": 15,
  "claro": 16,
  "movistar": 17,
  "tigo": 18,
  "container": 19,
  "andres capital": 20,
  "dream games": 21,
  "vpg sas": 22,
  "jop": 23,
  "gama case": 24,
  "l&m": 25,
  "raco": 26,
  "memorias musica": 27,
  "chocolocell": 28,
  "frente smart plus": 29,
  "safari": 30,
  "alg": 31,
  "pompas": 32,
  "110-chicago": 33,
  "jvd": 34,
  "ekady": 35,
  "tyd": 36,
  "sd tecnology": 37,
  "celuflex": 38,
  "global importaciones": 39,
  "tigerss nodo": 40,
  "eg accesorios": 41,
  "chicago 107": 42,
  "fyr flex": 43,
  "tablet store": 44,
  "tecno game": 45,
}
# opciones
opcion = int(input("-1 Agregar info -2 Consultar base "))

if opcion == 1:
  prov.append("iphone: xr")
else:
  contador = 0
  limite = 10
  while contador <= limite:
    consultar = input("Digita tu consulta: o digita exit para salir ...")
    if consultar == "exit":
        contador += 10
    else:
      valor = consultar
      resultado = prov.get(valor, "no hay resultados para esta consulta")
      contador += 1
      info = valor.upper()
      print (f"{info} = {resultado}")
      # print(f"Consulta {contador}")
      print(f"Consultas realizadas: {contador} te quedan {10 - contador}" )
      print("*=" * 25)

