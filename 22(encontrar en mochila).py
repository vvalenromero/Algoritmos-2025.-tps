def usar_la_fuerza(mochila, objetos_sacados=0):
    
    if len(mochila) == 0:
        print("No se encontró un sable de luz.")
        return False, objetos_sacados

    
    objeto = mochila.pop(0)
    objetos_sacados += 1
    print('buscando...')
    print(f"Objeto: {objeto}")

    
    if objeto == "sable de luz":
        print("Encontro el sable de luz")
        return True, objetos_sacados
    else:
        
        return usar_la_fuerza(mochila, objetos_sacados)



mochila = ["botella de agua", "comunicador", "cuerda", "sable de luz", "linterna"]


encontro_sable, cantidad_objetos = usar_la_fuerza(mochila)


print("\nResultado final:")
print(f"¿Se encontró el sable de luz? {encontro_sable}")
print(f"Cantidad de objetos sacados: {cantidad_objetos}")



