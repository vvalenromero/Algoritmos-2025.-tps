from typing import Any, Optional  # Importa tipos genéricos y opcionales para anotaciones de tipo
from tree import BinaryTree  # Importa la clase BinaryTree desde el módulo tree
from queue_ import Queue  # Importa la clase Queue desde el módulo queue_

creatures_data = [  # Lista de diccionarios con criaturas mitológicas y quién las derrotó
    {"name": "Ceto", "defeated_by": None}, {"name": "Tifón", "defeated_by": "Zeus"},  # Ceto sin vencedor, Tifón derrotado por Zeus
    {"name": "Equidna", "defeated_by": "Argos Panoptes"}, {"name": "Dino", "defeated_by": None},  # Equidna derrotada por Argos, Dino sin vencedor
    {"name": "Pefredo", "defeated_by": None}, {"name": "Enio", "defeated_by": None},  # Pefredo y Enio sin vencedor
    {"name": "Escila", "defeated_by": None}, {"name": "Caribdis", "defeated_by": None},  # Escila y Caribdis sin vencedor
    {"name": "Euríale", "defeated_by": None}, {"name": "Esteno", "defeated_by": None},  # Euríale y Esteno sin vencedor
    {"name": "Medusa", "defeated_by": "Perseo"}, {"name": "Ladón", "defeated_by": "Heracles"},  # Medusa derrotada por Perseo, Ladón por Heracles
    {"name": "Águila del Cáucaso", "defeated_by": None}, {"name": "Quimera", "defeated_by": "Belerofonte"},  # Águila sin vencedor, Quimera derrotada por Belerofonte
    {"name": "Hidra de Lerna", "defeated_by": "Heracles"}, {"name": "León de Nemea", "defeated_by": "Heracles"},  # Hidra y León de Nemea derrotados por Heracles
    {"name": "Esfinge", "defeated_by": "Edipo"}, {"name": "Dragón de la Cólquida", "defeated_by": None},  # Esfinge derrotada por Edipo, Dragón sin vencedor
    {"name": "Cerbero", "defeated_by": None}, {"name": "Cerda de Cromión", "defeated_by": "Teseo"},  # Cerbero sin vencedor, Cerda derrotada por Teseo
    {"name": "Ortro", "defeated_by": "Heracles"}, {"name": "Toro de Creta", "defeated_by": "Teseo"},  # Ortro por Heracles, Toro de Creta por Teseo
    {"name": "Jabalí de Calidón", "defeated_by": "Atalanta"}, {"name": "Carcinos", "defeated_by": None},  # Jabalí por Atalanta, Carcinos sin vencedor
    {"name": "Gerión", "defeated_by": "Heracles"}, {"name": "Cloto", "defeated_by": None},  # Gerión por Heracles, Cloto sin vencedor
    {"name": "Láquesis", "defeated_by": None}, {"name": "Átropos", "defeated_by": None},  # Láquesis y Átropos sin vencedor
    {"name": "Minotauro de Creta", "defeated_by": "Teseo"}, {"name": "Harpías", "defeated_by": None},  # Minotauro por Teseo, Harpías sin vencedor
    {"name": "Argos Panoptes", "defeated_by": "Hermes"}, {"name": "Aves del Estínfalo", "defeated_by": None},  # Argos por Hermes, Aves sin vencedor
    {"name": "Talos", "defeated_by": "Medea"}, {"name": "Sirenas", "defeated_by": None},  # Talos por Medea, Sirenas sin vencedor
    {"name": "Pitón", "defeated_by": "Apolo"}, {"name": "Cierva de Cerinea", "defeated_by": None},  # Pitón por Apolo, Cierva sin vencedor
    {"name": "Basilisco", "defeated_by": None}, {"name": "Jabalí de Erimanto", "defeated_by": None},  # Basilisco y Jabalí de Erimanto sin vencedor
]  # Fin de la lista de criaturas


def in_order_traverse(root, func):  # Define una función para recorrer el árbol en inorden y aplicar una función a cada nodo
    if root:  # Si el nodo actual existe
        in_order_traverse(root.left, func)  # Recorre recursivamente el subárbol izquierdo
        func(root)  # Aplica la función al nodo actual
        in_order_traverse(root.right, func)  # Recorre recursivamente el subárbol derecho


creature_tree = BinaryTree()  # Crea una instancia de BinaryTree para almacenar las criaturas

for creature in creatures_data:  # Recorre cada criatura de la lista de datos
    creature_info = {  # Construye un diccionario con información adicional de la criatura
        "defeated_by": creature["defeated_by"],  # Guarda quién la derrotó
        "description": "",  # Inicializa la descripción vacía
        "captured_by": None  # Inicializa el campo de capturado por como None
    }  # Fin del diccionario de información de la criatura
    creature_tree.insert(creature["name"], creature_info)  # Inserta la criatura en el árbol con su nombre como clave

print("Árbol de criaturas mitológicas generado.")  # Informa que el árbol fue generado exitosamente

# a. Listado inorden de las criaturas y quienes las derrotaron
print("\na. Listado inorden de criaturas:")  # Título para la sección a


def print_creature_info(node):  # Función que imprime la información básica de una criatura
    defeated_by = node.other_values.get("defeated_by") or "-"  # Obtiene quién la derrotó o '-' si no hay dato
    print(f"- {node.value} (Derrotado por: {defeated_by})")  # Imprime el nombre y su vencedor


in_order_traverse(creature_tree.root, print_creature_info)  # Recorre el árbol e imprime la info de cada criatura


# b. Cargar una breve descripción
print("\nb. Cargando descripción de la Medusa...")  # Indica que se cargará una descripción para Medusa
medusa_node = creature_tree.search("Medusa")  # Busca el nodo correspondiente a Medusa en el árbol
if medusa_node:  # Si se encontró el nodo de Medusa
    medusa_node.other_values["description"] = "Una de las tres gorgonas, la única mortal. Podía petrificar con la mirada."  # Asigna una descripción
    print("Descripción de Medusa cargada correctamente.")  # Informa que se cargó la descripción
else:  # Si no se encuentra Medusa en el árbol
    print("No se encontró a Medusa en el árbol.")  # Informa que Medusa no se encontró


# c. Mostrar toda la información de Talos
print("\nc. Información completa de Talos:")  # Título de la sección c
talos_node = creature_tree.search("Talos")  # Busca el nodo correspondiente a Talos
if talos_node:  # Si se encontró a Talos
    print(f"  Criatura: {talos_node.value}")  # Imprime el nombre de la criatura
    for key, value in talos_node.other_values.items():  # Recorre todos los campos adicionales del nodo
        print(f"  - {key.replace('_', ' ').capitalize()}: {value or 'No disponible'}")  # Imprime clave y valor formateados
else:  # Si no se encuentra Talos
    print("Talos no encontrado.")  # Informa que Talos no fue encontrado


# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nd. Top 3 héroes/dioses por criaturas derrotadas:")  # Título para la sección d
defeats_count = {}  # Diccionario para contar cuántas criaturas derrotó cada héroe/dios


def count_defeats(node):  # Función que suma derrotas por vencedor
    defeater = node.other_values.get("defeated_by")  # Obtiene el nombre de quien derrotó a la criatura
    if defeater:  # Si existe un vencedor
        defeats_count[defeater] = defeats_count.get(defeater, 0) + 1  # Incrementa el contador correspondiente


in_order_traverse(creature_tree.root, count_defeats)  # Recorre el árbol y cuenta las derrotas

top_defeaters = sorted(defeats_count.items(), key=lambda item: item[1], reverse=True)  # Ordena vencedores por cantidad de derrotas de mayor a menor
for i, (name, count) in enumerate(top_defeaters[:3]):  # Recorre los primeros 3 vencedores
    print(f"  {i+1}. {name} ({count} derrotas)")  # Imprime la posición, nombre y cantidad de derrotas


# e. Listar las criaturas derrotadas por Heracles
print("\ne. Criaturas derrotadas por Heracles:")  # Título para la sección e


def find_by_defeater(node):  # Función que imprime criaturas derrotadas por un vencedor específico
    if node.other_values.get("defeated_by") == "Heracles":  # Si el vencedor es Heracles
        print(f"- {node.value}")  # Imprime el nombre de la criatura


in_order_traverse(creature_tree.root, find_by_defeater)  # Recorre el árbol para encontrar criaturas derrotadas por Heracles


# f. Listar las criaturas que no han sido derrotadas
print("\nf. Criaturas que no han sido derrotadas:")  # Título para la sección f


def find_undefeated(node):  # Función que imprime criaturas sin vencedor
    if not node.other_values.get("defeated_by"):  # Si no hay valor en defeated_by
        print(f"- {node.value}")  # Imprime el nombre de la criatura


in_order_traverse(creature_tree.root, find_undefeated)  # Recorre el árbol buscando criaturas no derrotadas

# h. Modificar nodos para indicar capturas por Heracles
print("\nh. Actualizando criaturas capturadas por Heracles...")  # Título para la sección h
creatures_to_capture = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]  # Lista de criaturas que serán marcadas como capturadas por Heracles
for name in creatures_to_capture:  # Recorre cada nombre de criatura en la lista
    node = creature_tree.search(name)  # Busca el nodo de esa criatura
    if node:  # Si la criatura existe en el árbol
        node.other_values["captured_by"] = "Heracles"  # Marca que fue capturada por Heracles
print("Nodos de Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto actualizados.")  # Mensaje informando la actualización


# i. Búsquedas por coincidencia
print("\ni. Búsqueda por coincidencia para 'Ja':")  # Título para la sección i
# La función proximity_search en el archivo original ya imprime los resultados.
creature_tree.proximity_search("Ja")  # Llama a la función del árbol que busca por coincidencia con 'Ja'


# j. Eliminar al Basilisco y a las Sirenas
print("\nj. Eliminando a Basilisco y Sirenas...")  # Título para la sección j
creature_tree.delete("Basilisco")  # Elimina el nodo correspondiente a Basilisco del árbol
creature_tree.delete("Sirenas")  # Elimina el nodo correspondiente a Sirenas del árbol
print("Criaturas eliminadas.")  # Informa que las criaturas fueron eliminadas


# k. Modificar el nodo de las Aves del Estínfalo
print("\nk. Modificando información de las Aves del Estínfalo...")  # Título para la sección k
aves_node = creature_tree.search("Aves del Estínfalo")  # Busca el nodo de Aves del Estínfalo
if aves_node:  # Si el nodo existe
    aves_node.other_values["defeated_by"] = "Heracles"  # Marca que fueron derrotadas por Heracles
    aves_node.other_values["description"] = "Heracles derrotó a varias de ellas en su sexto trabajo."  # Agrega una descripción adicional
    print("Nodo de Aves del Estínfalo actualizado.")  # Informa que el nodo fue actualizado
else:  # Si no se encuentran las Aves del Estínfalo
    print("No se encontraron las Aves del Estínfalo.")  # Informa que no se encontró el nodo


# l. Modificar el nombre de Ladón por Dragón Ladón
print("\nl. Modificando el nombre de Ladón a Dragón Ladón...")  # Título para la sección l
value, other_values = creature_tree.delete("Ladón")  # Elimina el nodo de Ladón y guarda su valor e información adicional
if value:  # Si se encontró y eliminó a Ladón
    creature_tree.insert("Dragón Ladón", other_values)  # Inserta un nuevo nodo con el nombre actualizado y los mismos datos
    print("Nombre de Ladón modificado correctamente.")  # Informa que el cambio de nombre fue exitoso
else:  # Si no se encontró a Ladón
    print("No se encontró a Ladón para modificar.")  # Informa que no se pudo modificar porque no existe

# m. Realizar un listado por nivel del árbol
print("\nm. Listado del árbol por nivel:")  # Título para la sección m
creature_tree.by_level()  # Realiza un barrido por niveles del árbol e imprime cada nodo

# n. Mostrar las criaturas capturadas por Heracles
print("\nn. Criaturas capturadas por Heracles:")  # Título para la sección n


def find_captured_by_heracles(node):  # Función que imprime criaturas capturadas por Heracles
    if node.other_values.get("captured_by") == "Heracles":  # Si el campo captured_by es Heracles
        print(f"- {node.value}")  # Imprime el nombre de la criatura


in_order_traverse(creature_tree.root, find_captured_by_heracles)  # Recorre el árbol y muestra las criaturas capturadas por Heracles