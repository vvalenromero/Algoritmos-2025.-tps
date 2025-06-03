from stack import Stack


def obtener_posiciones_rocket_y_groot(stack):
    aux_stack = Stack()
    pos_rocket = None
    pos_groot = None
    pos = 1
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje[0] == "Rocket Raccoon":
            pos_rocket = pos
        if personaje[0] == "Groot":
            pos_groot = pos
        aux_stack.push(personaje)
        pos += 1
    restaurar_stack(stack, aux_stack)
    return pos_rocket, pos_groot

def mostrar_personajes_mas_de_peliculas(stack, min_peliculas):
    print(f"Personajes con más de {min_peliculas} películas:")
    aux_stack = Stack()
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje[1] > min_peliculas:
            print(f"{personaje[0]} - {personaje[1]} películas")
        aux_stack.push(personaje)
    restaurar_stack(stack, aux_stack)

def obtener_num_peliculas(stack, nombre):
    aux_stack = Stack()
    num_peliculas = None
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje[0] == nombre:
            num_peliculas = personaje[1]
        aux_stack.push(personaje)
    restaurar_stack(stack, aux_stack)
    return num_peliculas

def mostrar_personajes_por_inicial(stack, iniciales):
    print("Personajes cuyos nombres empiezan con:")
    for letra in iniciales:
        print(letra)

    aux_stack = Stack()
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje[0][0] in iniciales:
            print(personaje[0])
        aux_stack.push(personaje)
    restaurar_stack(stack, aux_stack)


    aux_stack = Stack()
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje[0][0] in iniciales:
            print(personaje[0])
        aux_stack.push(personaje)
    restaurar_stack(stack, aux_stack)

def restaurar_stack(original, auxiliar):
    while auxiliar.size() > 0:
        original.push(auxiliar.pop())


datos_mcu = [
    ("Rocket Raccoon", 6),
    ("Groot", 5),
    ("Tony Stark", 10),
    ("Steve Rogers", 9),
    ("Natasha Romanoff", 7),
    ("Carol Danvers", 4),
    ("Clint Barton", 6),
    ("Drax", 3),
    ("Gamora", 5),
    ("Doctor Strange", 4),
    ("Carol Danvers", 4),
]

pila_personajes = Stack()

for personaje in datos_mcu:
    pila_personajes.push(personaje)

print("Pila original de personajes:")
pila_personajes.show()

pos_rocket = obtener_posiciones_rocket_y_groot(pila_personajes)[0]
pos_groot = obtener_posiciones_rocket_y_groot(pila_personajes)[1]

if pos_rocket is not None:
    print("Posición de Rocket Raccoon en la pila:", pos_rocket)
else:
    print("Posición de Rocket Raccoon en la pila: No encontrado")

if pos_groot is not None:
    print("Posición de Groot en la pila:", pos_groot)
else:
    print("Posición de Groot en la pila: No encontrado")


mostrar_personajes_mas_de_peliculas(pila_personajes, 5)

if obtener_num_peliculas(pila_personajes, "Natasha Romanoff") is not None:
    print("Black Widow participó en", obtener_num_peliculas(pila_personajes, "Natasha Romanoff"), "películas.")
else:
    print("Black Widow no encontrada.")


mostrar_personajes_por_inicial(pila_personajes, ['C', 'D', 'G'])
