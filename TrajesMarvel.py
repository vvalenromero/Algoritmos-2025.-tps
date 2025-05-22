pila = [
    {"modelo": "Mark I", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Impecable"},
    {"modelo": "Mark VII", "pelicula": "The Avengers", "estado": "Destruido"},
    {"modelo": "Mark XXXV", "pelicula": "Iron Man 3", "estado": "Dañado"},
    {"modelo": "Mark XL", "pelicula": "Iron Man 3", "estado": "Impecable"},
    {"modelo": "Mark LXXX", "pelicula": "Avengers: Endgame", "estado": "Destruido"}
]

pila_original = pila.copy()

peliculas_hulkbuster = {item["pelicula"] for item in pila if item["modelo"] == "Mark XXXV"}

print(" Actividad 1 ")
if peliculas_hulkbuster:
    print("Mark XXXV fue utilizado en las siguientes películas:")
    for pelicula in peliculas_hulkbuster:
        print("-", pelicula)
else:
    print("Mark XXXV no fue utilizado en ninguna película.")

modelos_dañados = [item["modelo"] for item in pila if item["estado"] == "Dañado"]

print("Actividad 2 ")
print("Modelos dañados (sin alterar la pila):")
for modelo in modelos_dañados:
    print("-", modelo)

destruidos = [item for item in pila if item["estado"] == "Destruido"]
pila = [item for item in pila if item["estado"] != "Destruido"]

print("Actividad 3")
print("Modelos eliminados por estar destruidos:")
for d in destruidos:
    print("-", d["modelo"])

nuevo_traje = {"modelo": "Mark LXXX", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
pila.append(nuevo_traje)

print(" Actividad 4 ")
print("Modelo agregado a la pila:", nuevo_traje["modelo"])

peliculas_deseadas = {"Iron Man 2", "Iron Man 3"}
trajes_usados = [item["modelo"] for item in pila if item["pelicula"] in peliculas_deseadas]

print(" Actividad 5 ")
print("Trajes utilizados en las películas seleccionadas:")
for modelo in trajes_usados:
    print("-", modelo)

print(" Estado final de la pila ")
for traje in pila:
    print(traje)
