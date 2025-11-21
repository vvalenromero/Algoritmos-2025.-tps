
from graph import Graph
import math

ambientes = [
    'cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
    'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio'
]


distancias = [
    ('sala de estar', 'comedor', 4),
    ('sala de estar', 'habitación 1', 3),
    ('sala de estar', 'habitación 2', 3),
    ('sala de estar', 'baño 1', 2),
    ('sala de estar', 'terraza', 5),

    ('comedor', 'cocina', 3),
    ('comedor', 'quincho', 6),
    ('comedor', 'baño 2', 4),

    ('cocina', 'patio', 5),
    ('cocina', 'cochera', 7),

    ('habitación 1', 'baño 1', 2),
    ('habitación 1', 'terraza', 4),

    ('baño 1', 'habitación 2', 2),

    ('cochera', 'patio', 8),
    ('cochera', 'quincho', 10),

    ('quincho', 'patio', 3),
    ('quincho', 'terraza', 8),

    ('habitación 2', 'baño 2', 1),

]

casa = Graph(is_directed=False)

for ambiente in ambientes:
    casa.insert_vertex(ambiente)

for origen, destino, distancia in distancias:
    casa.insert_edge(origen, destino, distancia)

print("--- Grafo de la casa cargado ---\n")


print("--- c. Árbol de Expansión Mínima (Kruskal) ---")
print("Calculando la cantidad mínima de cable para conectar todos los ambientes:")

expansion_tree_str = casa.kruskal('cocina')
metros_de_cable_mst = 0

aristas_como_string = expansion_tree_str.split(';')
for arista_str in aristas_como_string:
    partes = arista_str.split('-')
    if len(partes) == 3:
        origen, destino, peso_str = partes
        peso = int(peso_str)
        metros_de_cable_mst += peso
        print(f"  - Conexión: {origen} <-> {destino}, Metros: {peso}")

print(f"\n>> Se necesitan un total de {metros_de_cable_mst} metros de cable para conectar todos los ambientes.\n")
print("="*60 + "\n")


print("--- d. Camino más corto para Router -> Smart TV ---")

def find_and_print_path(graph, origin, destination):
    path_stack = graph.dijkstra(origin)
    
    path_info = {}
    while path_stack.size() > 0:
        item = path_stack.pop()
        path_info[item[0]] = item
    
    if destination not in path_info or path_info[destination][1] == float('inf'):
        print(f"No se encontró un camino de '{origin}' a '{destination}'.")
        return

    path = []
    current_name = destination
    while current_name is not None:
        path.append(current_name)
        current_name = path_info[current_name][2]
    
    path.reverse()
    costo = path_info[destination][1]
    
    print(f"El camino más corto es: {' -> '.join(path)}")
    print(f">> Se necesitan {costo} metros de cable de red para conectar el router en '{origin}' con el Smart TV en '{destination}'.\n")

find_and_print_path(casa, 'habitación 1', 'sala de estar')