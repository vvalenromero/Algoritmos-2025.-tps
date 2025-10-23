from typing import Any, Optional
from tree import BinaryTree
from queue_ import Queue

creatures_data = [
    {"name": "Ceto", "defeated_by": None}, {"name": "Tifón", "defeated_by": "Zeus"},
    {"name": "Equidna", "defeated_by": "Argos Panoptes"}, {"name": "Dino", "defeated_by": None},
    {"name": "Pefredo", "defeated_by": None}, {"name": "Enio", "defeated_by": None},
    {"name": "Escila", "defeated_by": None}, {"name": "Caribdis", "defeated_by": None},
    {"name": "Euríale", "defeated_by": None}, {"name": "Esteno", "defeated_by": None},
    {"name": "Medusa", "defeated_by": "Perseo"}, {"name": "Ladón", "defeated_by": "Heracles"},
    {"name": "Águila del Cáucaso", "defeated_by": None}, {"name": "Quimera", "defeated_by": "Belerofonte"},
    {"name": "Hidra de Lerna", "defeated_by": "Heracles"}, {"name": "León de Nemea", "defeated_by": "Heracles"},
    {"name": "Esfinge", "defeated_by": "Edipo"}, {"name": "Dragón de la Cólquida", "defeated_by": None},
    {"name": "Cerbero", "defeated_by": None}, {"name": "Cerda de Cromión", "defeated_by": "Teseo"},
    {"name": "Ortro", "defeated_by": "Heracles"}, {"name": "Toro de Creta", "defeated_by": "Teseo"},
    {"name": "Jabalí de Calidón", "defeated_by": "Atalanta"}, {"name": "Carcinos", "defeated_by": None},
    {"name": "Gerión", "defeated_by": "Heracles"}, {"name": "Cloto", "defeated_by": None},
    {"name": "Láquesis", "defeated_by": None}, {"name": "Átropos", "defeated_by": None},
    {"name": "Minotauro de Creta", "defeated_by": "Teseo"}, {"name": "Harpías", "defeated_by": None},
    {"name": "Argos Panoptes", "defeated_by": "Hermes"}, {"name": "Aves del Estínfalo", "defeated_by": None},
    {"name": "Talos", "defeated_by": "Medea"}, {"name": "Sirenas", "defeated_by": None},
    {"name": "Pitón", "defeated_by": "Apolo"}, {"name": "Cierva de Cerinea", "defeated_by": None},
    {"name": "Basilisco", "defeated_by": None}, {"name": "Jabalí de Erimanto", "defeated_by": None},
]



def in_order_traverse(root, func):
    if root:
        in_order_traverse(root.left, func)
        func(root)
        in_order_traverse(root.right, func)

creature_tree = BinaryTree()

for creature in creatures_data:
    creature_info = {
        "defeated_by": creature["defeated_by"],
        "description": "", 
        "captured_by": None
    }
    creature_tree.insert(creature["name"], creature_info)

print("Árbol de criaturas mitológicas generado.")

# a. Listado inorden de las criaturas y quienes las derrotaron
print("\na. Listado inorden de criaturas:")
def print_creature_info(node):
    defeated_by = node.other_values.get("defeated_by") or "-"
    print(f"- {node.value} (Derrotado por: {defeated_by})")
in_order_traverse(creature_tree.root, print_creature_info)


# b. Cargar una breve descripción
print("\nb. Cargando descripción de la Medusa...")
medusa_node = creature_tree.search("Medusa")
if medusa_node:
    medusa_node.other_values["description"] = "Una de las tres gorgonas, la única mortal. Podía petrificar con la mirada."
    print("Descripción de Medusa cargada correctamente.")
else:
    print("No se encontró a Medusa en el árbol.")


# c. Mostrar toda la información de Talos
print("\nc. Información completa de Talos:")
talos_node = creature_tree.search("Talos")
if talos_node:
    print(f"  Criatura: {talos_node.value}")
    for key, value in talos_node.other_values.items():
        print(f"  - {key.replace('_', ' ').capitalize()}: {value or 'No disponible'}")
else:
    print("Talos no encontrado.")


# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nd. Top 3 héroes/dioses por criaturas derrotadas:")
defeats_count = {}
def count_defeats(node):
    defeater = node.other_values.get("defeated_by")
    if defeater:
        defeats_count[defeater] = defeats_count.get(defeater, 0) + 1
in_order_traverse(creature_tree.root, count_defeats)

top_defeaters = sorted(defeats_count.items(), key=lambda item: item[1], reverse=True)
for i, (name, count) in enumerate(top_defeaters[:3]):
    print(f"  {i+1}. {name} ({count} derrotas)")


# e. Listar las criaturas derrotadas por Heracles
print("\ne. Criaturas derrotadas por Heracles:")
def find_by_defeater(node):
    if node.other_values.get("defeated_by") == "Heracles":
        print(f"- {node.value}")
in_order_traverse(creature_tree.root, find_by_defeater)


# f. Listar las criaturas que no han sido derrotadas
print("\nf. Criaturas que no han sido derrotadas:")
def find_undefeated(node):
    if not node.other_values.get("defeated_by"):
        print(f"- {node.value}")
in_order_traverse(creature_tree.root, find_undefeated)

# h. Modificar nodos para indicar capturas por Heracles
print("\nh. Actualizando criaturas capturadas por Heracles...")
creatures_to_capture = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
for name in creatures_to_capture:
    node = creature_tree.search(name)
    if node:
        node.other_values["captured_by"] = "Heracles"
print("Nodos de Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto actualizados.")


# i. Búsquedas por coincidencia
print("\ni. Búsqueda por coincidencia para 'Ja':")
# La función proximity_search en el archivo original ya imprime los resultados.
creature_tree.proximity_search("Ja")


# j. Eliminar al Basilisco y a las Sirenas
print("\nj. Eliminando a Basilisco y Sirenas...")
creature_tree.delete("Basilisco")
creature_tree.delete("Sirenas")
print("Criaturas eliminadas.")


# k. Modificar el nodo de las Aves del Estínfalo
print("\nk. Modificando información de las Aves del Estínfalo...")
aves_node = creature_tree.search("Aves del Estínfalo")
if aves_node:
    aves_node.other_values["defeated_by"] = "Heracles"
    aves_node.other_values["description"] = "Heracles derrotó a varias de ellas en su sexto trabajo."
    print("Nodo de Aves del Estínfalo actualizado.")
else:
    print("No se encontraron las Aves del Estínfalo.")


# l. Modificar el nombre de Ladón por Dragón Ladón
print("\nl. Modificando el nombre de Ladón a Dragón Ladón...")
value, other_values = creature_tree.delete("Ladón")
if value:
    creature_tree.insert("Dragón Ladón", other_values)
    print("Nombre de Ladón modificado correctamente.")
else:
    print("No se encontró a Ladón para modificar.")

# m. Realizar un listado por nivel del árbol
print("\nm. Listado del árbol por nivel:")
creature_tree.by_level()

# n. Mostrar las criaturas capturadas por Heracles
print("\nn. Criaturas capturadas por Heracles:")
def find_captured_by_heracles(node):
    if node.other_values.get("captured_by") == "Heracles":
        print(f"- {node.value}")
in_order_traverse(creature_tree.root, find_captured_by_heracles)