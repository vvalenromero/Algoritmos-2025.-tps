def usar_la_fuerza(mochila, objetos_sacados=0):
    # Si la mochila está vacía
    if len(mochila) == 0:
        print("No se encontró un sable de luz.")
        return False, objetos_sacados

    # Sacar el primer objeto
    objeto = mochila.pop(0)
    objetos_sacados += 1
    print('buscando...')
    print(f"Objeto: {objeto}")

    # Si el objeto es un sable de luz, terminamos
    if objeto == "sable de luz":
        print("Encontro el sable de luz")
        return True, objetos_sacados
    else:
        # Si no, seguir buscando
        return usar_la_fuerza(mochila, objetos_sacados)


# Crear la mochila con objetos
mochila = ["botella de agua", "comunicador", "cuerda", "sable de luz", "linterna"]

# Llamar a la función
encontro_sable, cantidad_objetos = usar_la_fuerza(mochila)

# Mostrar el resultado final
print("\nResultado final:")
print(f"¿Se encontró el sable de luz? {encontro_sable}")
print(f"Cantidad de objetos sacados: {cantidad_objetos}")



