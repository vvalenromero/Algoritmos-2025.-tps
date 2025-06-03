def romano_a_decimal(romano, indice=0, total=0):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if indice == len(romano) - 1:
        return total + valores[romano[indice]]

    actual = valores[romano[indice]]
    siguiente = valores[romano[indice + 1]]

    if actual < siguiente:
        total -= actual
    else:
        total += actual

    return romano_a_decimal(romano, indice + 1, total)


entrada = input("Ingresa un número romano en mayúsculas (ej: XIV, MCM): ")
resultado = romano_a_decimal(entrada)
print("El número decimal equivalente es:", resultado)
