from cgi import print_form
from ctypes.wintypes import PINT
from operator import index

huawei = ["Y9 prime", "Y9 2019", "P20 lite", "Psmart", "A7 2019"]
xiaomi = ["Note 11", "Redmi 10", "Redmi 9a", "Note 8 pro", "Redmi 7"]
samsung = ["A31", "A21s", "A13 4g", "A12", "A03 core"]

size = len(xiaomi)
# print(size)
# print(type(xiaomi))
# print(xiaomi)


user = input("ref .. ")
usercap = user.capitalize()


if usercap in (xiaomi):
    indice = xiaomi.index(usercap)
    print(
        f"El {usercap} es el numero {indice + 1} de la lista de referencias registradas de XIAOMI"
    )
elif usercap in (samsung):
    indice = samsung.index(usercap)
    print(
        f"El {usercap} es el numero {indice + 1} de la lista de referencias registradas de SAMSUNG"
    )
elif usercap in (huawei):
    indice = huawei.index(usercap)
    print(
        f"El {usercap} es el numero {indice + 1} de la lista de referencias registradas de HUAWEI"
    )
else:
    print("Ese valor no existe")
