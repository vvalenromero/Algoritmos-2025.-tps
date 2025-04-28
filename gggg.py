def romano_a_decimal(romano):
    # Crear un diccionario que asocia cada letra romana con su valor decimal
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0  # Acá vamos a ir sumando el número final
    anterior = 0  # Guarda el valor anterior para comparar
    
    # Recorrer el número romano de derecha a izquierda
    for letra in reversed(romano):
        valor_actual = valores_romanos[letra]  # Buscar el valor de la letra en el diccionario
        
        if valor_actual < anterior:
            # Si el valor actual es menor que el anterior, se resta
            total = total - valor_actual
        else:
            # Si el valor actual es igual o mayor que el anterior, se suma
            total = total + valor_actual
        
        # Actualizar el valor anterior para la próxima comparación
        anterior = valor_actual
    
    return total

# Ahora pedimos al usuario que ingrese un número romano
numero_romano = input("Ingresá un número romano: ").upper()  # .upper() convierte lo que escribas a mayúsculas
resultado = romano_a_decimal(numero_romano)
print(f"El número decimal es: {resultado}")





