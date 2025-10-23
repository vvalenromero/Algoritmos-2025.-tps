from tree import BinaryTree
from typing import Any, Optional
from queue import Queue
from lista import List

def heroes_start_with(self, letter: str):
        """c. Muestra superhéroes que empiezan con una letra."""
        def __heroes_start_with(root, letter):
            if root is not None:
                __heroes_start_with(root.left, letter)
                if not root.other_values['is_villain'] and root.value.startswith(letter):
                    print(f"- {root.value}")
                __heroes_start_with(root.right, letter)
        __heroes_start_with(self.root, letter)

def heroes_in_order_desc(self):
        """f. Lista superhéroes en orden alfabético descendente."""
        def __heroes_in_order_desc(root):
            if root is not None:
                __heroes_in_order_desc(root.right)
                if not root.other_values['is_villain']:
                    print(f"- {root.value}")
                __heroes_in_order_desc(root.left)
        __heroes_in_order_desc(self.root)

def count_nodes(self) -> int:
        """g.I. Cuenta el número total de nodos en el árbol."""
        def __count_nodes(root):
            return 0 if root is None else 1 + __count_nodes(root.left) + __count_nodes(root.right)
        return __count_nodes(self.root)

def in_order_names(self):
        """g.II. Realiza un barrido alfabético mostrando solo nombres."""
        def __in_order_names(root):
            if root is not None:
                __in_order_names(root.left)
                print(f"- {root.value}")
                __in_order_names(root.right)
        __in_order_names(self.root)

    
#main


mcu_arbol = BinaryTree()
personajes = [
    {'name': 'Iron Man', 'is_villain': False},
    {'name': 'Thanos', 'is_villain': True},
    {'name': 'Captain America', 'is_villain': False},
    {'name': 'Red Skull', 'is_villain': True},
    {'name': 'Hulk', 'is_villain': False},
    {'name': 'Loki', 'is_villain': True},
    {'name': 'Thor', 'is_villain': False},
    {'name': 'Doctor Estranio', 'is_villain': False},
    {'name': 'Black Widow', 'is_villain': False},
    {'name': 'Ultron', 'is_villain': True},
    {'name': 'Spider-Man', 'is_villain': False},
    {'name': 'Captain Marvel', 'is_villain': False},
    {'name': 'Dormammu', 'is_villain': True},
    {'name': 'Scarlet Witch', 'is_villain': False}
]

for p in personajes:
    mcu_arbol.insert(p['name'], p)

print("Árbol MCU cargado con éxito.")

print("\n--- b. Villanos ordenados alfabéticamente ---")
mcu_arbol.villain_in_order()

print("\n--- c. Superhéroes que empiezan con la letra 'C' ---")
mcu_arbol.heroes_start_with('Captain')

print("\n--- d. Cantidad de superhéroes en el árbol ---")
num_heroes = mcu_arbol.count_heroes()
print(f"El árbol contiene {num_heroes} superhéroes.")

print("\n--- e. Corregir 'Doctor Estranio' por 'Doctor Strange' ---")
value, other_values = mcu_arbol.delete('Doctor Estranio')
if value is not None:
    other_values['name'] = 'Doctor Strange'
    mcu_arbol.insert('Doctor Strange', other_values)
    print("Se ha corregido el nombre 'Doctor Estranio' a 'Doctor Strange'.")
else:
    print("No se encontró a 'Doctor Estranio' para corregir.")

print("\n--- f. Superhéroes ordenados de manera descendente ---")
mcu_arbol.heroes_in_order_desc()

print("\n--- g. Generación de un bosque a partir del árbol principal ---")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()
mcu_arbol.divide_tree(arbol_heroes, arbol_villanos)
print("Se han generado dos nuevos árboles: uno para héroes y otro para villanos.")

print("\n--- g.I. Conteo de nodos en cada árbol del bosque ---")
print(f"El árbol de héroes tiene {arbol_heroes.count_nodes()} nodos.")
print(f"El árbol de villanos tiene {arbol_villanos.count_nodes()} nodos.")

print("\n--- g.II. Barrido alfabético de cada árbol del bosque ---")
print("\n   Héroes (orden alfabético):")
arbol_heroes.in_order_names()

print("\n   Villanos (orden alfabético):")
arbol_villanos.in_order_names()