from stack import Stack



def obtener_peliculas_mark(stack, mark):
    aux_stack = Stack()
    peliculas = []
    while stack.size() > 0:
        traje = stack.pop()
        if traje[0] == mark:
            peliculas.append(traje[1])
        aux_stack.push(traje)
    restaurar_stack(stack, aux_stack)
    return peliculas

def mostrar_modelos_danados(stack):
    print("Modelos dañados:")
    aux_stack = Stack()
    while stack.size() > 0:
        traje = stack.pop()
        if traje[2] == "Dañado":
            print(traje)
        aux_stack.push(traje)
    restaurar_stack(stack, aux_stack)

def eliminar_modelos_destruidos(stack):
    print("Modelos destruidos eliminados:")
    aux_stack = Stack()
    while stack.size() > 0:
        traje = stack.pop()
        if traje[2] == "Destruido":
            print(traje[0])
        else:
            aux_stack.push(traje)
    restaurar_stack(stack, aux_stack)

def agregar_traje_si_no_existe(stack, nuevo_traje):
    aux_stack = Stack()
    repetido = False
    while stack.size() > 0:
        traje = stack.pop()
        if traje[0] == nuevo_traje[0] and traje[1] == nuevo_traje[1]:
            repetido = True
        aux_stack.push(traje)
    restaurar_stack(stack, aux_stack)
    if not repetido:
        stack.push(nuevo_traje)
        print("Se agregó el traje", nuevo_traje[0])
    else:
        print("Ya existe", nuevo_traje[0], "para la película", nuevo_traje[1])

def modelos_por_pelicula(stack, peliculas_objetivo):
    resultados = {pelicula: [] for pelicula in peliculas_objetivo}
    aux_stack = Stack()
    while stack.size() > 0:
        traje = stack.pop()
        if traje[1] in peliculas_objetivo:
            resultados[traje[1]].append(traje[0])
        aux_stack.push(traje)
    restaurar_stack(stack, aux_stack)
    for pelicula in peliculas_objetivo:
        print(f"Modelos usados en {pelicula}:")
        for modelo in resultados[pelicula]:
            print(f" - {modelo}")

def restaurar_stack(original, auxiliar):
    while auxiliar.size() > 0:
        original.push(auxiliar.pop())


datos = [
    ("Mark III", "Iron Man", "Dañado"),
    ("Mark XLIV", "Avengers: Age of Ultron", "Dañado"),
    ("Mark XLIV", "Avengers: Infinity War", "Impecable"),
    ("Mark L", "Avengers: Infinity War", "Destruido"),
    ("Mark VII", "The Avengers", "Dañado"),
    ("Mark XL", "Spider-Man: Homecoming", "Impecable"),
    ("Mark XLVI", "Capitan America: Civil War", "Dañado"),
]

trajes_stack = Stack()

for traje in datos:
    trajes_stack.push(traje)

print("Pila original de trajes:")
trajes_stack.show()

peliculas_mark_xliv = obtener_peliculas_mark(trajes_stack, "Mark XLIV")
if peliculas_mark_xliv:
    print("Mark XLIV fue usado en las películas:", peliculas_mark_xliv)
else:
    print("Mark XLIV no fue usado en ninguna película.")

mostrar_modelos_danados(trajes_stack)

eliminar_modelos_destruidos(trajes_stack)

nuevo_traje = ("Mark LXXXV", "Avengers: Endgame", "Impecable")
agregar_traje_si_no_existe(trajes_stack, nuevo_traje)

peliculas_objetivo = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
modelos_por_pelicula(trajes_stack, peliculas_objetivo)
