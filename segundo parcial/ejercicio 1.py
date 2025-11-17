from tree import BinaryTree

pokemon_data = [
    {'nombre': 'Bulbasaur', 'número': 1, 'tipos': ['Planta', 'Veneno'], 'debilidades': ['Fuego', 'Volador', 'Hielo', 'Psíquico'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Charmander', 'número': 4, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Charizard', 'número': 6, 'tipos': ['Fuego', 'Volador'], 'debilidades': ['Agua', 'Eléctrico', 'Roca'], 'megaevolucion': True, 'gigamax': True},
    {'nombre': 'Squirtle', 'número': 7, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Pikachu', 'número': 25, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Jolteon', 'número': 135, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'megaevolucion': False, 'gigamax': False},
    {'nombre': 'Gengar', 'número': 94, 'tipos': ['Fantasma', 'Veneno'], 'debilidades': ['Fantasma', 'Siniestro', 'Psíquico', 'Tierra'], 'megaevolucion': True, 'gigamax': True},
    {'nombre': 'Steelix', 'número': 208, 'tipos': ['Acero', 'Tierra'], 'debilidades': ['Fuego', 'Agua', 'Lucha', 'Tierra'], 'megaevolucion': True, 'gigamax': False},
    {'nombre': 'Lycanroc', 'número': 745, 'tipos': ['Roca'], 'debilidades': ['Agua', 'Planta', 'Lucha', 'Tierra', 'Acero'], 'megaevolucion': False, 'gigamax': False},
    {'nombre': 'Tyrantrum', 'número': 697, 'tipos': ['Roca', 'Dragón'], 'debilidades': ['Hada', 'Dragón', 'Hielo', 'Lucha', 'Tierra', 'Acero'], 'megaevolucion': False, 'gigamax': False},
    {'nombre': 'Bulbizarre', 'número': 1026, 'tipos': ['Planta', 'Veneno'], 'debilidades': ['Fuego', 'Volador', 'Hielo', 'Psíquico'], 'megaevolucion': False, 'gigamax': False}, # Para prueba de proximidad
]

# --- 1. Creación de los tres árboles ---
tree_name = BinaryTree()
tree_number = BinaryTree()
tree_type = BinaryTree()

# Poblar los árboles con los datos
for pokemon in pokemon_data:
    tree_name.insert(pokemon['nombre'], pokemon)
    tree_number.insert(pokemon['número'], pokemon)
    for tipo in pokemon['tipos']:
        # Insertamos una entrada por cada tipo que tenga el Pokémon
        tree_type.insert(tipo, pokemon)


def search_by_proximity(substring):
    """
    Muestra los datos de los Pokémon cuyos nombres contienen el substring.
    """
    print(f"--- Búsqueda por proximidad para '{substring}' ---")
    def __in_order_search(root, value):
        if root is not None:
            __in_order_search(root.left, value)
            if value.lower() in root.value.lower():
                print(f"  - {root.value}: {root.other_values}")
            __in_order_search(root.right, value)
    
    __in_order_search(tree_name.root, substring)

def show_pokemon_by_types(types_to_show):
    """
    Muestra los nombres de los Pokémon de los tipos especificados.
    """
    print(f"--- Pokémon de tipo {', '.join(types_to_show)} ---")
    def __in_order_by_type(root, types):
        if root is not None:
            __in_order_by_type(root.left, types)
            if root.value in types:
                print(f"  - Tipo: {root.value}, Pokémon: {root.other_values['nombre']}")
            __in_order_by_type(root.right, types)
            
    __in_order_by_type(tree_type.root, types_to_show)

def show_weak_against(pokemon_names):
    """
    Muestra todos los Pokémon que son débiles a los tipos de los Pokémon dados.
    """
    print(f"--- Pokémon débiles frente a {', '.join(pokemon_names)} ---")
    weakness_types = set()
    for name in pokemon_names:
        node = tree_name.search(name)
        if node:
            for tipo in node.other_values['tipos']:
                weakness_types.add(tipo)
    
    print(f"Tipos a buscar debilidad: {list(weakness_types)}")

    def __in_order_check_weakness(root, types):
        if root is not None:
            __in_order_check_weakness(root.left, types)
            # Comprobar si hay alguna debilidad en común
            if set(root.other_values['debilidades']) & types:
                print(f"  - {root.value} es débil contra uno de los tipos.")
            __in_order_check_weakness(root.right, types)

    __in_order_check_weakness(tree_name.root, weakness_types)

def count_and_show_types():
    """
    Cuenta cuántos Pokémon hay de cada tipo y lo muestra.
    """
    print("--- Conteo de Pokémon por tipo ---")
    type_counts = {}
    def __in_order_count(root, counts):
        if root is not None:
            __in_order_count(root.left, counts)
            tipo = root.value
            counts[tipo] = counts.get(tipo, 0) + 1
            __in_order_count(root.right, counts)
    
    __in_order_count(tree_type.root, type_counts)
    
    for tipo, count in type_counts.items():
        print(f"  - Tipo {tipo}: {count} Pokémon")

def count_property(prop_name):
    """
    Función genérica para contar Pokémon con una propiedad booleana (megaevolucion, gigamax).
    """
    def __in_order_count_prop(root):
        count = 0
        if root is not None:
            if root.other_values[prop_name]:
                count += 1
            count += __in_order_count_prop(root.left)
            count += __in_order_count_prop(root.right)
        return count
        
    return __in_order_count_prop(tree_name.root)


# --- Ejecución de las soluciones ---

# 2. Mostrar datos de un Pokémon por su número y nombre
print("--- Búsqueda por número (25) ---")
pikachu = tree_number.search(25)
if pikachu:
    print(pikachu.other_values)
print()

search_by_proximity("Bulb")
print()

# 3. Mostrar nombres de Pokémon de tipos específicos
show_pokemon_by_types(['Fantasma', 'Fuego', 'Acero', 'Eléctrico'])
print()

# 4. Listados en orden ascendente y por nivel
print("--- Listado por número (ascendente) ---")
tree_number.in_order()
print("\n--- Listado por nombre (ascendente) ---")
tree_name.in_order()
print("\n--- Listado por nivel (usando el árbol de nombres) ---")
tree_name.by_level()
print()

# 5. Mostrar Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum
show_weak_against(['Jolteon', 'Lycanroc', 'Tyrantrum'])
print()

# 6. Mostrar todos los tipos y cuántos hay de cada uno
count_and_show_types()
print()

# 7. Determinar cuántos Pokémon tienen megaevolucion
mega_count = count_property('megaevolucion')
print(f"--- Cantidad de Pokémon con Megaevolución: {mega_count} ---")
print()

# 8. Determinar cuántos Pokémon tienen forma gigamax
gigamax_count = count_property('gigamax')
print(f"--- Cantidad de Pokémon con forma Gigamax: {gigamax_count} ---")
print()