def romano_a_decimal(romano):
    valores_romanos = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }
    
    total = 0  
    anterior = 0  
    
    
    for letra in reversed(romano):
        valor_actual = valores_romanos[letra]  
        
        if valor_actual < anterior:
            
            total = total - valor_actual
        else:
            
            total = total + valor_actual
        
        
        anterior = valor_actual
    
    return total


numero_romano = input("Ingresá un número romano: ")
resultado = romano_a_decimal(numero_romano)
print(f"El número decimal es: {resultado}")


