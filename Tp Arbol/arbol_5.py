from typing import Any, Optional  # Importa tipos genéricos Any y Optional para anotaciones de tipo
from queue_ import Queue  # Importa la clase Queue definida en el módulo queue_
from tree import BinaryTree  # Importa la clase BinaryTree definida en el módulo tree
from stack import Stack  # Importa la clase Stack definida en el módulo stack


def heroes_starting_with_c(arbol):  # Define una función que muestra héroes que empiezan con 'C'
    def __heroes_starting_with_c(root):  # Función interna recursiva que recorre el árbol
        if root:  # Si el nodo actual no es None
            __heroes_starting_with_c(root.left)  # Recorre recursivamente el subárbol izquierdo
            if not root.other_values.get("is_villain") and root.value.startswith('C'):  # Si no es villano y el nombre empieza con 'C'
                print(root.value)  # Imprime el nombre del personaje
            __heroes_starting_with_c(root.right)  # Recorre recursivamente el subárbol derecho

    __heroes_starting_with_c(arbol.root)  # Llama a la función recursiva comenzando desde la raíz del árbol


def heroes_in_descending_order(arbol):  # Define una función que muestra héroes en orden alfabético descendente
    def __heroes_in_descending_order(root):  # Función interna recursiva que recorre el árbol
        if root:  # Si el nodo actual no es None
            __heroes_in_descending_order(root.right)  # Recorre primero el subárbol derecho para obtener orden descendente
            if not root.other_values.get("is_villain"):  # Si el personaje no es villano
                print(root.value)  # Imprime el nombre del héroe
            __heroes_in_descending_order(root.left)  # Recorre luego el subárbol izquierdo

    __heroes_in_descending_order(arbol.root)  # Llama a la función recursiva comenzando desde la raíz


def count_nodes(arbol):  # Define una función que cuenta la cantidad de nodos en un árbol
    def __count_nodes(root):  # Función interna recursiva que cuenta los nodos
        return 1 + __count_nodes(root.left) + __count_nodes(root.right) if root else 0  # Si el nodo existe, cuenta 1 más sus subárboles, si no, 0

    return __count_nodes(arbol.root)  # Devuelve el total de nodos tomando como inicio la raíz


print("LISTA ORIGINAL DE PERSONAJES")  # Muestra un título para la lista original de personajes
mcu_characters = [  # Lista de diccionarios con personajes del MCU y si son villanos o no
    {'name': 'Iron Man', 'is_villain': False},  # Personaje Iron Man, no villano
    {'name': 'Thanos', 'is_villain': True},  # Personaje Thanos, villano
    {'name': 'Captain America', 'is_villain': False},  # Personaje Captain America, no villano
    {'name': 'Red Skull', 'is_villain': True},  # Personaje Red Skull, villano
    {'name': 'Thor', 'is_villain': False},  # Personaje Thor, no villano
    {'name': 'Loki', 'is_villain': True},  # Personaje Loki, villano
    {'name': 'Hulk', 'is_villain': False},  # Personaje Hulk, no villano
    {'name': 'Black Widow', 'is_villain': False},  # Personaje Black Widow, no villano
    {'name': 'Dr Strange', 'is_villain': False},  # Personaje Dr Strange, no villano
    {'name': 'Captain Marvel', 'is_villain': False},  # Personaje Captain Marvel, no villano
    {'name': 'Ultron', 'is_villain': True},  # Personaje Ultron, villano
    {'name': 'Dormammu', 'is_villain': True},  # Personaje Dormammu, villano
]  # Fin de la lista de personajes
for char in mcu_characters:  # Itera sobre cada personaje de la lista
    print(f"- {char['name']} (Villano: {char['is_villain']})")  # Imprime el nombre y si es villano


mcu_tree = BinaryTree()  # Crea una instancia de BinaryTree para almacenar los personajes
for char in mcu_characters:  # Recorre cada personaje en la lista
    mcu_tree.insert(char['name'], char)  # Inserta el personaje en el árbol usando el nombre como clave
print("\na. Árbol de personajes de MCU creado y poblado.")  # Informa que el árbol fue creado y cargado

# b. Listar villanos ordenados alfabéticamente
print("\nb. Villanos ordenados alfabéticamente:")  # Muestra el título de la sección b
mcu_tree.villain_in_order()  # Llama al método del árbol que muestra villanos en orden alfabético

# c. Mostrar todos los superhéroes que empiezan con C
print("\nc. Superhéroes que empiezan con C:")  # Muestra el título de la sección c
heroes_starting_with_c(mcu_tree)  # Llama a la función que imprime héroes cuyos nombres comienzan con 'C'

# f. Listar los superhéroes ordenados de manera descendente
print("\nf. Superhéroes ordenados de manera descendente:")  # Muestra el título de la sección f
heroes_in_descending_order(mcu_tree)  # Llama a la función que imprime héroes en orden descendente

# g. Generar un bosque a partir del árbol principal
print("\ng. Generando bosque de héroes y villanos...")  # Informa que se está generando un bosque
heroes_tree = BinaryTree()  # Crea un árbol binario para héroes
villains_tree = BinaryTree()  # Crea un árbol binario para villanos
mcu_tree.divide_tree(heroes_tree, villains_tree)  # Divide el árbol principal en dos: héroes y villanos
print("Bosque generado.")  # Informa que el bosque se generó correctamente

# g.I. Determinar cuántos nodos tiene cada árbol
print(f"Nodos en el árbol de héroes: {count_nodes(heroes_tree)}")  # Imprime la cantidad de nodos del árbol de héroes
print(f"Nodos en el árbol de villanos: {count_nodes(villains_tree)}")  # Imprime la cantidad de nodos del árbol de villanos

# g.II. Realizar un barrido ordenado alfabéticamente de cada árbol
print("\nII. Barrido ordenado de cada árbol:")  # Título para el barrido ordenado de cada árbol
print("\n Héroes (alfabéticamente) ")  # Título para el barrido de héroes
heroes_tree.in_order()  # Realiza barrido inorden sobre el árbol de héroes
print(" Villanos (alfabéticamente) ")  # Título para el barrido de villanos
villains_tree.in_order()  # Realiza barrido inorden sobre el árbol de villanos


print("LISTA FINAL DE PERSONAJES")  # Título para la lista final de personajes
print("Contenido del árbol principal después de los cambios (ordenado alfabéticamente):")  # Explica lo que se mostrará a continuación

stack = []  # Inicializa una lista vacía que se usará como pila para recorrido iterativo inorden
current_node = mcu_tree.root  # Comienza el recorrido desde la raíz del árbol principal
while current_node is not None or len(stack) > 0:  # Mientras exista un nodo actual o la pila no esté vacía
    while current_node is not None:  # Baja por la rama izquierda del árbol
        stack.append(current_node)  # Apila el nodo actual
        current_node = current_node.left  # Avanza al hijo izquierdo

    current_node = stack.pop()  # Toma el último nodo apilado (retrocede un nivel)
    print(f"- {current_node.value} (Villano: {current_node.other_values.get('is_villain', 'N/A')})")  # Imprime el valor del nodo y si es villano
    current_node = current_node.right  # Cambia al hijo derecho del nodo actual para continuar el recorrido