pila = [
    {'nombre': 'Iron Man', 'peliculas': 10},
    {'nombre': 'Rocket Raccoon', 'peliculas': 6},
    {'nombre': 'Groot', 'peliculas': 6},
    {'nombre': 'Black Widow', 'peliculas': 7},
    {'nombre': 'Doctor Strange', 'peliculas': 5},
    {'nombre': 'Captain America', 'peliculas': 9},
    {'nombre': 'Gamora', 'peliculas': 4},
    {'nombre': 'Hulk', 'peliculas': 8},
    {'nombre': 'Drax', 'peliculas': 4}
]
pila_original = pila.copy()

print(" Actividad 1 ")
objetivos = ["Rocket Raccoon", "Groot"]
posiciones = {}
tamaño = len(pila)
pos = 1
indice = tamaño - 1
while indice >= 0:
    personaje = pila[indice]
    if personaje["nombre"] in objetivos:
        posiciones[personaje["nombre"]] = pos
    pos += 1
    indice -= 1

for nombre in objetivos:
    if nombre in posiciones:
        print(f"{nombre} está en la posición {posiciones[nombre]}")
    else:
        print(f"{nombre} no está en la pila")

print(" Actividad 2 ")
print("Personajes con más de 5 películas:")
for item in pila:
    if item["peliculas"] > 5:
        print(f"- {item['nombre']}: {item['peliculas']} películas")

print(" Actividad 3 ")
encontrado = False
for item in pila:
    if item["nombre"] == "Black Widow":
        print(f"Black Widow participó en {item['peliculas']} películas")
        encontrado = True
        break
if not encontrado:
    print("Black Widow no se encuentra en la pila")

print(" Actividad 4 ")
iniciales = ("C", "D", "G")
seleccionados = []
i = 0
while i < len(pila):
    if pila[i]["nombre"].startswith(iniciales):
        seleccionados.append(pila[i]["nombre"])
    i += 1

print("Personajes cuyos nombres empiezan con C, D o G:")
for nombre in seleccionados:
    print("-", nombre)

print(" Estado final de la pila ")
for personaje in pila:
    print(personaje)
