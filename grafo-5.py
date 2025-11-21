from graph import Graph
import math

class GraphModificado(Graph):
    
    def insert_vertex(self, value: any, other_values: any = None) -> None:
        """
        Esta es la nueva versión del método que permite guardar datos adicionales.
        """
        node_vertex = self._Graph__nodeVertex(value, other_values)
        self.append(node_vertex)


g = GraphModificado(is_directed=False)


nodes_data = [
    ('Manjaro', {'type': 'pc'}), ('Parrot', {'type': 'pc'}), ('Fedora', {'type': 'pc'}),
    ('Ubuntu', {'type': 'pc'}), ('Mint', {'type': 'pc'}),
    ('Red Hat', {'type': 'notebook'}), ('Debian', {'type': 'notebook'}), ('Arch', {'type': 'notebook'}),
    ('Impresora', {'type': 'impresora'}),
    ('Guaraní', {'type': 'servidor'}), ('MongoDB', {'type': 'servidor'}),
    ('Switch 1', {'type': 'switch'}), ('Switch 2', {'type': 'switch'}),
    ('Router 1', {'type': 'router'}), ('Router 2', {'type': 'router'}), ('Router 3', {'type': 'router'})
]

edges_data = [
    ('Red Hat', 'Guaraní', 9), ('Red Hat', 'Router 2', 25), ('Debian', 'Switch 1', 17),
    ('Ubuntu', 'Switch 1', 18), ('Impresora', 'Switch 1', 22), ('Mint', 'Switch 1', 80),
    ('Switch 1', 'Router 1', 29), ('Router 1', 'Router 2', 37), ('Router 1', 'Router 3', 43),
    ('Guaraní', 'Router 3', 50), ('Manjaro', 'Router 3', 40), ('Router 3', 'Switch 2', 61),
    ('Switch 2', 'Parrot', 12), ('Switch 2', 'Fedora', 3), ('Switch 2', 'Arch', 5),
    ('Switch 2', 'MongoDB', 56)
]

for name, data in nodes_data:
    g.insert_vertex(name, other_values=data) 

for origin, dest, weight in edges_data:
    g.insert_edge(origin, dest, weight)

print("--- Grafo de red cargado ---\n")

print("--- b. Barridos desde las notebooks ---")
notebooks = ['Red Hat', 'Debian', 'Arch']
for nb in notebooks:
    print(f"\n>> Barrido en Profundidad (DFS) desde '{nb}':")
    g.deep_sweep(nb)
    print(f"\n>> Barrido en Amplitud (BFS) desde '{nb}':")
    g.amplitude_sweep(nb)
print("\n" + "="*40 + "\n")

# --- Función auxiliar para mostrar caminos de Dijkstra ---
def find_and_print_path(graph, origin, destination):
    path_stack = graph.dijkstra(origin)
    path_info = {}
    while path_stack.size() > 0:
        item = path_stack.pop()
        path_info[item[0]] = item
    
    if destination not in path_info or path_info[destination][1] == math.inf:
        print(f"No se encontró un camino de '{origin}' a '{destination}'.")
        return None, math.inf

    path, current_name = [], destination
    while current_name is not None:
        path.append(current_name)
        current_name = path_info[current_name][2]
    path.reverse()
    cost = path_info[destination][1]
    
    print(f"Camino de '{origin}' a '{destination}': {' -> '.join(path)} (Costo: {cost})")
    return path, cost

print("--- c. Caminos más cortos a la Impresora ---")
pcs_to_print = ['Manjaro', 'Red Hat', 'Fedora']
for pc in pcs_to_print:
    find_and_print_path(g, pc, 'Impresora')
print("\n" + "="*40 + "\n")

print("--- d. Árbol de Expansión Mínima (Kruskal) ---")

expansion_tree_str = g.kruskal('Manjaro') 
total_weight = 0

aristas_como_string = expansion_tree_str.split(';')

for arista_str in aristas_como_string:
    partes = arista_str.split('-')
    if len(partes) == 3:
        origin, dest, weight_str = partes
        weight = int(weight_str)
        
        total_weight += weight
        print(f"  - Arista: {origin} <-> {dest}, Peso: {weight}")

print(f"Costo total del árbol de expansión: {total_weight}\n")
print("="*40 + "\n")
print("="*40 + "\n")

print("--- e. Camino más corto desde una PC al servidor 'Guaraní' ---")
min_cost = math.inf
best_path_info = None
pcs = [node.value for node in g if node.other_values['type'] == 'pc']
for pc in pcs:
    path, cost = find_and_print_path(g, pc, 'Guaraní')
    if cost < min_cost:
        min_cost = cost
        best_path_info = (pc, path)

if best_path_info:
    print(f"\n>> El camino más corto es desde '{best_path_info[0]}' con un costo de {min_cost}.")
print("\n" + "="*40 + "\n")

print("--- f. Camino más corto desde una PC en Switch 1 al servidor 'MongoDB' ---")
min_cost_sw1 = math.inf
best_path_info_sw1 = None
switch1_pos = g.search('Switch 1', 'value')
if switch1_pos is not None:
    computers_on_sw1 = [edge.value for edge in g[switch1_pos].edges if g[g.search(edge.value, 'value')].other_values['type'] in ['pc', 'notebook']]
    for comp in computers_on_sw1:
        path, cost = find_and_print_path(g, comp, 'MongoDB')
        if cost < min_cost_sw1:
            min_cost_sw1 = cost
            best_path_info_sw1 = (comp, path)

if best_path_info_sw1:
    print(f"\n>> El camino más corto desde el Switch 1 es desde '{best_path_info_sw1[0]}' con un costo de {min_cost_sw1}.")
print("\n" + "="*40 + "\n")

print("--- g. Cambiando conexión de la Impresora a Router 2 ---")
g.delete_edge('Impresora', 'Switch 1')
g.insert_edge('Impresora', 'Router 2', 19)
print("Conexión modificada. Resolviendo el punto b nuevamente:")

for nb in notebooks:
    print(f"\n>> Barrido en Profundidad (DFS) desde '{nb}':")
    g.deep_sweep(nb)
    print(f"\n>> Barrido en Amplitud (BFS) desde '{nb}':")
    g.amplitude_sweep(nb)
print("\n" + "="*40 + "\n")