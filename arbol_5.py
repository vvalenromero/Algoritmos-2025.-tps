from typing import Any, Optional
from queue_ import Queue
from tree import BinaryTree
from stack import Stack

def heroes_starting_with_c(arbol):
    def __heroes_starting_with_c(root):
        if root:
            __heroes_starting_with_c(root.left)
            if not root.other_values.get("is_villain") and root.value.startswith('C'):
                print(root.value)
            __heroes_starting_with_c(root.right)
    __heroes_starting_with_c(arbol.root) 
    
def heroes_in_descending_order(arbol):
    def __heroes_in_descending_order(root):
        if root:
            __heroes_in_descending_order(root.right)
            if not root.other_values.get("is_villain"): 
                print(root.value)
            __heroes_in_descending_order(root.left)
    __heroes_in_descending_order(arbol.root) 

def count_nodes(arbol):
    def __count_nodes(root):
        return 1 + __count_nodes(root.left) + __count_nodes(root.right) if root else 0
    return __count_nodes(arbol.root) 


print("LISTA ORIGINAL DE PERSONAJES")
mcu_characters = [
    {'name': 'Iron Man', 'is_villain': False},
    {'name': 'Thanos', 'is_villain': True},
    {'name': 'Captain America', 'is_villain': False},
    {'name': 'Red Skull', 'is_villain': True},
    {'name': 'Thor', 'is_villain': False},
    {'name': 'Loki', 'is_villain': True},
    {'name': 'Hulk', 'is_villain': False},
    {'name': 'Black Widow', 'is_villain': False},
    {'name': 'Dr Strange', 'is_villain': False},
    {'name': 'Captain Marvel', 'is_villain': False},
    {'name': 'Ultron', 'is_villain': True},
    {'name': 'Dormammu', 'is_villain': True},
]
for char in mcu_characters:
    print(f"- {char['name']} (Villano: {char['is_villain']})")


mcu_tree = BinaryTree()
for char in mcu_characters:
    mcu_tree.insert(char['name'], char)
print("\na. Árbol de personajes de MCU creado y poblado.")

# b. Listar villanos ordenados alfabéticamente
print("\nb. Villanos ordenados alfabéticamente:")
mcu_tree.villain_in_order()

# c. Mostrar todos los superhéroes que empiezan con C
print("\nc. Superhéroes que empiezan con C:")
heroes_starting_with_c(mcu_tree) 

# f. Listar los superhéroes ordenados de manera descendente
print("\nf. Superhéroes ordenados de manera descendente:")
heroes_in_descending_order(mcu_tree) 

# g. Generar un bosque a partir del árbol principal
print("\ng. Generando bosque de héroes y villanos...")
heroes_tree = BinaryTree()
villains_tree = BinaryTree()
mcu_tree.divide_tree(heroes_tree, villains_tree) 
print("Bosque generado.")

# g.I. Determinar cuántos nodos tiene cada árbol
print(f"Nodos en el árbol de héroes: {count_nodes(heroes_tree)}") 
print(f"Nodos en el árbol de villanos: {count_nodes(villains_tree)}")

# g.II. Realizar un barrido ordenado alfabéticamente de cada árbol
print("\nII. Barrido ordenado de cada árbol:")
print("\n Héroes (alfabéticamente) ")
heroes_tree.in_order()
print(" Villanos (alfabéticamente) ")
villains_tree.in_order()


print("LISTA FINAL DE PERSONAJES")
print("Contenido del árbol principal después de los cambios (ordenado alfabéticamente):")

stack = []
current_node = mcu_tree.root
while current_node is not None or len(stack) > 0:
    while current_node is not None:
        stack.append(current_node)
        current_node = current_node.left
    
    current_node = stack.pop()
    print(f"- {current_node.value} (Villano: {current_node.other_values.get('is_villain', 'N/A')})")
    current_node = current_node.right