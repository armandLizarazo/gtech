
select = int(
    input(
        """
Seleccionar accion 
-1 Recargas 
-2 Modelos
-3 Clientes
"""
    )
)


if select == 1:
    import recargas

    print(recargas)
elif select == 2:
    import pedido

    print(pedido)
else:
    print("Opcion no valida")
