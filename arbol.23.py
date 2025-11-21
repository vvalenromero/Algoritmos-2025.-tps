from tree import BinaryTree  # Importa la clase BinaryTree desde el módulo tree
from typing import Any, Optional  # Importa tipos genéricos y opcionales para anotaciones
from queue import Queue  # Importa la clase Queue de la librería estándar (no se usa en este archivo)
from lista import List  # Importa la clase List definida en el módulo lista (no se usa en este archivo)


def heroes_start_with(self, letter: str):  # Define una función que debería ser método: muestra héroes que empiezan con una letra dada
        """c. Muestra superhéroes que empiezan con una letra."""  # Docstring que explica el propósito de la función
        def __heroes_start_with(root, letter):  # Función interna recursiva que recorre el árbol
            if root is not None:  # Si el nodo actual existe
                __heroes_start_with(root.left, letter)  # Recorre primero el subárbol izquierdo
                if not root.other_values['is_villain'] and root.value.startswith(letter):  # Si no es villano y comienza con la letra indicada
                    print(f"- {root.value}")  # Imprime el nombre del superhéroe
                __heroes_start_with(root.right, letter)  # Recorre luego el subárbol derecho

        __heroes_start_with(self.root, letter)  # Llama a la función recursiva desde la raíz del árbol


def heroes_in_order_desc(self):  # Define una función que debería ser método: lista héroes en orden alfabético descendente
        """f. Lista superhéroes en orden alfabético descendente."""  # Docstring que describe la función
        def __heroes_in_order_desc(root):  # Función interna recursiva que recorre el árbol
            if root is not None:  # Si el nodo actual existe
                __heroes_in_order_desc(root.right)  # Recorre primero el subárbol derecho (para orden descendente)
                if not root.other_values['is_villain']:  # Si el nodo no representa un villano
                    print(f"- {root.value}")  # Imprime el nombre del héroe
                __heroes_in_order_desc(root.left)  # Recorre luego el subárbol izquierdo

        __heroes_in_order_desc(self.root)  # Inicia el recorrido desde la raíz del árbol


def count_nodes(self) -> int:  # Define una función que debería ser método: cuenta nodos del árbol
        """g.I. Cuenta el número total de nodos en el árbol."""  # Docstring que explica la funcionalidad
        def __count_nodes(root):  # Función interna recursiva que cuenta cada nodo
            return 0 if root is None else 1 + __count_nodes(root.left) + __count_nodes(root.right)  # Si el nodo es None devuelve 0, sino 1 más sus subárboles

        return __count_nodes(self.root)  # Devuelve el total de nodos a partir de la raíz


def in_order_names(self):  # Define una función que debería ser método: recorre e imprime solo nombres en orden alfabético
        """g.II. Realiza un barrido alfabético mostrando solo nombres."""  # Docstring que describe el propósito
        def __in_order_names(root):  # Función interna recursiva para recorrido inorden
            if root is not None:  # Si el nodo existe
                __in_order_names(root.left)  # Recorre el subárbol izquierdo
                print(f"- {root.value}")  # Imprime el valor del nodo (nombre del personaje)
                __in_order_names(root.right)  # Recorre el subárbol derecho

        __in_order_names(self.root)  # Inicia el recorrido desde la raíz


# main


mcu_arbol = BinaryTree()  # Crea una instancia de BinaryTree que almacenará personajes del MCU
personajes = [  # Lista de diccionarios con personajes y si son villanos o no
    {'name': 'Iron Man', 'is_villain': False},  # Iron Man, no villano
    {'name': 'Thanos', 'is_villain': True},  # Thanos, villano
    {'name': 'Captain America', 'is_villain': False},  # Captain America, no villano
    {'name': 'Red Skull', 'is_villain': True},  # Red Skull, villano
    {'name': 'Hulk', 'is_villain': False},  # Hulk, no villano
    {'name': 'Loki', 'is_villain': True},  # Loki, villano
    {'name': 'Thor', 'is_villain': False},  # Thor, no villano
    {'name': 'Doctor Estranio', 'is_villain': False},  # Doctor Estranio (nombre mal escrito), no villano
    {'name': 'Black Widow', 'is_villain': False},  # Black Widow, no villano
    {'name': 'Ultron', 'is_villain': True},  # Ultron, villano
    {'name': 'Spider-Man', 'is_villain': False},  # Spider-Man, no villano
    {'name': 'Captain Marvel', 'is_villain': False},  # Captain Marvel, no villano
    {'name': 'Dormammu', 'is_villain': True},  # Dormammu, villano
    {'name': 'Scarlet Witch', 'is_villain': False}  # Scarlet Witch, no villano
]  # Fin de la lista de personajes

for p in personajes:  # Recorre cada personaje de la lista
    mcu_arbol.insert(p['name'], p)  # Inserta el personaje en el árbol usando el nombre como clave

print("Árbol MCU cargado con éxito.")  # Muestra un mensaje indicando que el árbol se cargó correctamente

print("\n--- b. Villanos ordenados alfabéticamente ---")  # Título de la sección b
mcu_arbol.villain_in_order()  # Llama al método del árbol para listar villanos en orden alfabético

print("\n--- c. Superhéroes que empiezan con la letra 'C' ---")  # Título de la sección c
mcu_arbol.heroes_start_with('Captain')  # Llama al método para listar héroes cuyo nombre empieza con 'Captain'

print("\n--- d. Cantidad de superhéroes en el árbol ---")  # Título de la sección d
num_heroes = mcu_arbol.count_heroes()  # Llama a un método del árbol que cuenta la cantidad de héroes
print(f"El árbol contiene {num_heroes} superhéroes.")  # Imprime el número total de héroes en el árbol

print("\n--- e. Corregir 'Doctor Estranio' por 'Doctor Strange' ---")  # Título de la sección e
value, other_values = mcu_arbol.delete('Doctor Estranio')  # Elimina el nodo con el nombre mal escrito y obtiene sus datos
if value is not None:  # Si se encontró y eliminó a 'Doctor Estranio'
    other_values['name'] = 'Doctor Strange'  # Corrige el nombre en el diccionario de datos
    mcu_arbol.insert('Doctor Strange', other_values)  # Inserta nuevamente el personaje con el nombre corregido
    print("Se ha corregido el nombre 'Doctor Estranio' a 'Doctor Strange'.")  # Informa que la corrección fue exitosa
else:  # Si no se encontró al personaje
    print("No se encontró a 'Doctor Estranio' para corregir.")  # Muestra un mensaje indicando que no se pudo corregir

print("\n--- f. Superhéroes ordenados de manera descendente ---")  # Título de la sección f
mcu_arbol.heroes_in_order_desc()  # Llama al método que lista héroes en orden alfabético descendente

print("\n--- g. Generación de un bosque a partir del árbol principal ---")  # Título de la sección g
arbol_heroes = BinaryTree()  # Crea un nuevo árbol para almacenar únicamente héroes
arbol_villanos = BinaryTree()  # Crea un nuevo árbol para almacenar únicamente villanos
mcu_arbol.divide_tree(arbol_heroes, arbol_villanos)  # Divide el árbol principal en dos: héroes y villanos
print("Se han generado dos nuevos árboles: uno para héroes y otro para villanos.")  # Informa que los árboles fueron generados

print("\n--- g.I. Conteo de nodos en cada árbol del bosque ---")  # Título de la sección g.I
print(f"El árbol de héroes tiene {arbol_heroes.count_nodes()} nodos.")  # Imprime la cantidad de nodos en el árbol de héroes
print(f"El árbol de villanos tiene {arbol_villanos.count_nodes()} nodos.")  # Imprime la cantidad de nodos en el árbol de villanos

print("\n--- g.II. Barrido alfabético de cada árbol del bosque ---")  # Título de la sección g.II
print("\n   Héroes (orden alfabético):")  # Título para el listado de héroes
arbol_heroes.in_order_names()  # Realiza un barrido inorden del árbol de héroes mostrando solo nombres

print("\n   Villanos (orden alfabético):")  # Título para el listado de villanos
arbol_villanos.in_order_names()  # Realiza un barrido inorden del árbol de villanos mostrando solo nombres