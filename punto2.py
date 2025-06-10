from superheroesProfe import superheroes
from typing import Any, Optional
from lista import List
from cola import Queue
from stack import Stack

def extraer_nombre(heroe):
    return str(heroe["name"])

def listar_ordenado_por_nombre(lista):
    return sorted(lista, key=extraer_nombre)  

ordenados = listar_ordenado_por_nombre(superheroes)

def encontrar_posicion(lista, nombre, indice=0):
    if indice >= len(lista):
        return None
    if lista[indice]["name"] == nombre:
        return str(indice + 1)
    return encontrar_posicion(lista, nombre, indice + 1)

pos_thing  = encontrar_posicion(superheroes, "The Thing")
pos_rocket = encontrar_posicion(superheroes, "Rocket Raccoon")

lista_personajes = List()
for personaje in superheroes:
    lista_personajes.append(personaje)

def filtrar_villanos(lista):
    villanos = List()
    for i in range(len(lista)):
        personaje = lista[i]
        if personaje["is_villain"]:
            villanos.append(personaje)
    return villanos

villanos = filtrar_villanos(lista_personajes)

cola_villanos = Queue()
for villano in villanos:
    cola_villanos.arrive(villano)

villanos_antes_1980 = []
cantidad = cola_villanos.size()
i = 0
while i < cantidad:
    villano = cola_villanos.attention()
    if villano["first_appearance"] < 1980:
        villanos_antes_1980.append(villano)
    i += 1

prefijos = ["Bl", "G", "My", "W"]
pila_filtrados = Stack()

for i in range(len(lista_personajes)):
    heroe = lista_personajes[i]
    for j in range(len(prefijos)):
        prefijo = prefijos[j]
        if heroe["name"].startswith(prefijo) or heroe["alias"].startswith(prefijo):
            pila_filtrados.push(heroe)
            break  

def extraer_nombre_real(personaje):
    return str(personaje["real_name"])

lista_personajes.add_criterion("nombre_real", extraer_nombre_real)
lista_personajes.sort_by_criterion("nombre_real")

def extraer_fecha_aparicion(personaje):
    return int(personaje["first_appearance"])

lista_personajes.add_criterion("fecha_aparicion", extraer_fecha_aparicion)
lista_personajes.sort_by_criterion("fecha_aparicion")

for i in range(len(lista_personajes)):
    personaje = lista_personajes[i]
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        break

def criterio_nombre(personaje):
    return str(personaje["name"])

lista_personajes.add_criterion("name", criterio_nombre)
eliminar_electro = lista_personajes.delete_value("Electro", "name")
eliminar_zemo = lista_personajes.delete_value("Baron Zemo", "name")


print("\nListado ordenado por nombre:")
for heroe in ordenados:
    print(str(heroe["name"]))

print(f"\nThe Thing está en la posición {pos_thing}")
print(f"\nRocket Raccoon está en la posición {pos_rocket}")

print("\nListado de villanos:")
villanos.show()

print("\nVillanos que aparecieron antes de 1980:")
for villano in villanos_antes_1980:
    print(f"{villano['name']} (Año: {villano['first_appearance']})")

print("\nSuperhéroes cuyo nombre o alias comienza con Bl, G, My, o W:")
pila_filtrados.show()

print("\nListado ordenado por nombre real (ascendente):")
lista_personajes.sort_by_criterion("nombre_real")
lista_personajes.show()

print("\nListado ordenado por fecha de aparición (ascendente):")
lista_personajes.sort_by_criterion("fecha_aparicion")
lista_personajes.show()

print("\nNombre real de Ant Man modificado a Scott Lang:")
for i in range(len(lista_personajes)):
    personaje = lista_personajes[i]
    if personaje["name"] == "Ant Man":
        print(personaje)

if eliminar_electro is not None:
    print("\nInformación de Electro eliminada:")
    print(eliminar_electro)
else:
    print("\nElectro no estaba en la lista.")

if eliminar_zemo is not None:
    print("\nInformación de Baron Zemo eliminada:")
    print(eliminar_zemo)
else:
    print("\nBaron Zemo no estaba en la lista.")

print("\nLista de personajes luego de eliminar a Electro y Baron Zemo:")
lista_personajes.show()
