def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return False, indice  

    if mochila[indice] == "sable de luz":
        return True, indice + 1  
    return usar_la_fuerza(mochila, indice + 1)



mochila = ["radio", "cuerda", "agua", "manta", "sable de luz"]
encontrado, objetos_usados = usar_la_fuerza(mochila)

if encontrado:
    print("¡Sable de luz encontrado!")
    print("Objetos sacados hasta encontrarlo:", objetos_usados)
else:
    print("No hay sable de luz en la mochila.")
    print("Objetos revisados:", objetos_usados)
