
from graph_modif import Graph

characters_data = {
    'Luke Skywalker': {'episodes': [3, 4, 5, 6, 7, 8, 9]},
    'Darth Vader': {'episodes': [1, 2, 3, 4, 5, 6]},
    'Yoda': {'episodes': [1, 2, 3, 5, 6, 8, 9]},
    'Boba Fett': {'episodes': [2, 4, 5, 6]},
    'C-3PO': {'episodes': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    'Leia': {'episodes': [3, 4, 5, 6, 7, 8, 9]},
    'Rey': {'episodes': [7, 8, 9]},
    'Kylo Ren': {'episodes': [7, 8, 9]},
    'Chewbacca': {'episodes': [3, 4, 5, 6, 7, 8, 9]},
    'Han Solo': {'episodes': [4, 5, 6, 7, 9]},
    'R2-D2': {'episodes': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    'BB-8': {'episodes': [7, 8, 9]}
}


edges_data = [
    ('Luke Skywalker', 'Leia', 4),
    ('Luke Skywalker', 'Darth Vader', 3),
    ('Luke Skywalker', 'Yoda', 2),
    ('Han Solo', 'Chewbacca', 5),
    ('Han Solo', 'Leia', 4),
    ('C-3PO', 'R2-D2', 9),
    ('Leia', 'C-3PO', 6),
    ('Darth Vader', 'Boba Fett', 2),
    ('Rey', 'Kylo Ren', 3),
    ('Rey', 'BB-8', 3),
    ('Yoda', 'C-3PO', 4)
]


g = Graph(is_directed=False)

# Cargamos los vértices (personajes) con sus datos adicionales
for name, data in characters_data.items():
    g.insert_vertex(name, other_values=data)

# Cargamos las aristas (relaciones)
for origin, dest, weight in edges_data:
    g.insert_edge(origin, dest, weight)

print("--- 1. Árbol de Expansión Mínimo (Kruskal) ---")

expansion_tree_str = g.kruskal('C-3PO')
total_weight = 0
mst_nodes = set()

aristas_como_string = expansion_tree_str.split(';')

for arista_str in aristas_como_string:
    partes = arista_str.split('-')
    if len(partes) == 3:
        origin, dest, weight_str = partes
        weight = int(weight_str)
        
        total_weight += weight
        mst_nodes.add(origin)
        mst_nodes.add(dest)
        print(f"  - Arista: {origin} <-> {dest}, Peso: {weight}")

    aristas_como_string = expansion_tree_str.split(';')

for arista_str in aristas_como_string:
    partes = arista_str.split('-')
    if len(partes) == 3:
        origin, dest, weight_str = partes
        weight = int(weight_str)
        
        total_weight += weight
        mst_nodes.add(origin)
        mst_nodes.add(dest)
        print(f"  - Arista: {origin} <-> {dest}, Peso: {weight}")
    total_weight += weight
    mst_nodes.add(origin)
    mst_nodes.add(dest)
    print(f"  - Arista: {origin} <-> {dest}, Peso: {weight}")

print(f"Peso total del árbol de expansión mínimo: {total_weight}")

required_chars = {'C-3PO', 'Yoda', 'Leia'}
if required_chars.issubset(mst_nodes):
    print("El árbol de expansión mínimo CONTIENE a C-3PO, Yoda y Leia.\n")
else:
    print("El árbol de expansión mínimo NO CONTIENE a todos los personajes requeridos.\n")


#  2. Determinar el número máximo de episodios que comparten dos personajes 
print("--- 2. Máximo número de episodios compartidos ---")
max_episodes = 0
max_pairs = []
processed_pairs = set()

for vertex in g:
    for edge in vertex.edges:
        pair = tuple(sorted((vertex.value, edge.value)))
        if pair not in processed_pairs:
            if edge.weight > max_episodes:
                max_episodes = edge.weight
                max_pairs = [pair]
            elif edge.weight == max_episodes:
                max_pairs.append(pair)
            processed_pairs.add(pair)

print(f"El número máximo de episodios compartidos es: {max_episodes}")
print("Los pares de personajes que coinciden son:")
for p1, p2 in max_pairs:
    print(f"  - {p1} y {p2}")
print()


# --- 3. Calcular el camino más corto (Dijkstra) ---
def find_and_print_path(graph, origin, destination):
    """
    Función auxiliar para procesar la pila de Dijkstra y mostrar el camino.
    """
    path_stack = graph.dijkstra(origin)
    
    path_info = {}
    while path_stack.size() > 0:
        item = path_stack.pop()
        path_info[item[0]] = item

    if destination not in path_info or path_info[destination][1] == float('inf'):
        print(f"No se encontró un camino de '{origin}' a '{destination}'.\n")
        return

    path = []
    current_name = destination
    while current_name is not None:
        path.append(current_name)
        current_name = path_info[current_name][2] # Vamos al nodo anterior

    path.reverse()
    cost = path_info[destination][1]
    
    print(f"Camino más corto de '{origin}' a '{destination}': {' -> '.join(path)}")
    print(f"Costo total (episodios en común en el camino): {cost}\n")

print("--- 3. Caminos más cortos (Dijkstra) ---")
find_and_print_path(g, 'C-3PO', 'R2-D2')
find_and_print_path(g, 'Yoda', 'Darth Vader')


print("--- 4. Personajes que aparecieron en los 9 episodios ---")
found_any = False
for vertex in g:
    # Accedemos a los datos adicionales guardados en el vértice
    if vertex.other_values and len(vertex.other_values.get('episodes', [])) == 9:
        print(f"  - {vertex.value}")
        found_any = True

if not found_any:
    print("Ningún personaje en los datos cargados apareció en los 9 episodios.")
print()