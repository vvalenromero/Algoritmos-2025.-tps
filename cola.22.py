from cola import Queue
cola = Queue()

cola.arrive(("Tony Stark", "Iron Man", "M"))
cola.arrive(("Steve Rogers", "Capitán América", "M"))
cola.arrive(("Natasha Romanoff", "Black Widow", "F"))
cola.arrive(("Carol Danvers", "Capitana Marvel", "F"))
cola.arrive(("Scott Lang", "Ant-Man", "M"))
cola.arrive(("Wanda Maximoff", "Scarlet Witch", "F"))
cola.arrive(("Sam Wilson", "Falcon", "M"))

def nombre_personaje_capitana_marvel(q: Queue):
    encontrado = None
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[1] == "Capitana Marvel":
            encontrado = personaje[0]
        q.arrive(personaje)
    return encontrado

def nombres_superheroes_femeninos(q: Queue):
    femeninos = []
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[2] == "F":
            femeninos.append(personaje[1])
        q.arrive(personaje)
    return femeninos

def nombres_personajes_masculinos(q: Queue):
    masculinos = []
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[2] == "M":
            masculinos.append(personaje[0])
        q.arrive(personaje)
    return masculinos

def nombre_superheroe_scott_lang(q: Queue):
    encontrado = None
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[0] == "Scott Lang":
            encontrado = personaje[1]
        q.arrive(personaje)
    return encontrado

def datos_nombres_empiezan_S(q: Queue):
    datos = []
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[0].startswith("S") or personaje[1].startswith("S"):
            datos.append(personaje)
        q.arrive(personaje)
    return datos

def buscar_carol_danvers(q: Queue):
    encontrado = None
    for i in range(q.size()):
        personaje = q.attention()
        if personaje[0] == "Carol Danvers":
            encontrado = personaje[1]
        q.arrive(personaje)
    if encontrado is None:
        return "No se encontró a Carol Danvers"
    else:
        return encontrado


print("a) Nombre del personaje de Capitana Marvel:", nombre_personaje_capitana_marvel(cola))
print("b) Nombres de superhéroes femeninos:", nombres_superheroes_femeninos(cola))
print("c) Nombres de personajes masculinos:", nombres_personajes_masculinos(cola))
print("d) Nombre del superhéroe de Scott Lang:", nombre_superheroe_scott_lang(cola))
print("e) Datos cuyos nombres empiezan con S:", datos_nombres_empiezan_S(cola))
print("f) Buscar Carol Danvers:", buscar_carol_danvers(cola))
