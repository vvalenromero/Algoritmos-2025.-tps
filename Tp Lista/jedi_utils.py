
jedis = [
    {"nombre": "Luke Skywalker", "maestros": ["Obi-Wan Kenobi", "Yoda"], "colores_sable": ["verde", "azul"], "especie": "Humano"},
    {"nombre": "Anakin Skywalker", "maestros": ["Obi-Wan Kenobi", "Qui-Gon Jinn"], "colores_sable": ["azul"], "especie": "Humano"},
    {"nombre": "Yoda", "maestros": [], "colores_sable": ["verde"], "especie": "Desconocida"},
    {"nombre": "Obi-Wan Kenobi", "maestros": ["Qui-Gon Jinn", "Yoda"], "colores_sable": ["azul"], "especie": "Humano"},
    {"nombre": "Mace Windu", "maestros": ["Cyslin Myr"], "colores_sable": ["violeta"], "especie": "Humano"},
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], "colores_sable": ["verde", "blanco"], "especie": "Togruta"},
    {"nombre": "Kit Fisto", "maestros": ["Yoda"], "colores_sable": ["verde"], "especie": "Nautolano"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Conde Dooku"], "colores_sable": ["verde"], "especie": "Humano"},
    {"nombre": "Plo Koon", "maestros": ["Tyvokka"], "colores_sable": ["azul"], "especie": "Kel Dor"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], "colores_sable": ["azul"], "especie": "Twi'lek"},
    {"nombre": "Ki-Adi-Mundi", "maestros": ["Yoda"], "colores_sable": ["azul"], "especie": "Cereano"},
    {"nombre": "Luminara Unduli", "maestros": [], "colores_sable": ["verde"], "especie": "Mirialan"},
    {"nombre": "Barriss Offee", "maestros": ["Luminara Unduli"], "colores_sable": ["azul", "rojo"], "especie": "Mirialan"},
    {"nombre": "Rey", "maestros": ["Luke Skywalker", "Leia Organa"], "colores_sable": ["amarillo", "azul"], "especie": "Humano"}
]


def ordenar_por_nombre(lista_jedis):
    return sorted(lista_jedis, key=lambda jedi: jedi["nombre"])

def ordenar_por_especie(lista_jedis):
    return sorted(lista_jedis, key=lambda jedi: jedi["especie"])

def mostrar_informacion(lista_jedis, nombres):
    for jedi in lista_jedis:
        if jedi["nombre"] in nombres:
            print(f"Información de {jedi['nombre']}:")
            for clave, valor in jedi.items():
                print(f"  - {clave.capitalize()}: {valor}")
            print()

def mostrar_padawans(lista_jedis, maestros):
    print(f"Padawans de {', '.join(maestros)}:")
    for jedi in lista_jedis:
        for maestro in maestros:
            if maestro in jedi["maestros"]:
                print(f"  - {jedi['nombre']} (aprendiz de {maestro})")

def mostrar_jedi_por_especie(lista_jedis, especies):
    print(f"Jedi de especie {' o '.join(especies)}:")
    for jedi in lista_jedis:
        if jedi["especie"] in especies:
            print(f"  - {jedi['nombre']}")

def listar_jedi_por_inicial(lista_jedis, inicial):
    print(f"Jedi cuyo nombre comienza con '{inicial}':")
    for jedi in lista_jedis:
        if jedi["nombre"].startswith(inicial):
            print(f"  - {jedi['nombre']}")

def mostrar_jedi_con_multiples_colores_sable(lista_jedis):
    print("Jedi que usaron sable de luz de más de un color:")
    for jedi in lista_jedis:
        if len(jedi["colores_sable"]) > 1:
            print(f"  - {jedi['nombre']} (Colores: {', '.join(jedi['colores_sable'])})")

def indicar_jedi_por_color_sable(lista_jedis, colores):
    print(f"Jedi que utilizaron sable de luz {' o '.join(colores)}:")
    for jedi in lista_jedis:
        for color in colores:
            if color in jedi["colores_sable"]:
                print(f"  - {jedi['nombre']} (usó {color})")
                break

def indicar_padawans_de_maestros(lista_jedis, nombres_maestros):
    for maestro in nombres_maestros:
        padawans = [jedi["nombre"] for jedi in lista_jedis if maestro in jedi["maestros"]]
        if padawans:
            print(f"Padawans de {maestro}: {', '.join(padawans)}")
        else:
            print(f"{maestro} no tuvo padawans en esta lista.")