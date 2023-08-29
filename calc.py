def suma_acumulada():
    numeros = []  # Lista para almacenar los números ingresados
    while True:
        entrada = input("Ingresa un número (o '=' para obtener el resultado total): ")
        
        if entrada.lower() == '=':
            resultado_suma = sum(numeros)
            print("El resultado total es:", resultado_suma)
            break  # Salir del ciclo while
        else:
            try:
                numero = float(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida. Ingresa un número válido o 'calcular'.")

# Llamar a la función para comenzar la suma acumulada
suma_acumulada()
