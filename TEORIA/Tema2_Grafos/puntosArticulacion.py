from collections import defaultdict


def find_articulation_points(g):
    """
    Encuentra los puntos de articulación en un grafo no dirigido.
    Un punto de articulación es un vértice cuya eliminación aumenta el número de componentes conexos.

    Args:
        g (dict): Grafo representado como diccionario de adyacencia

    Returns:
        set: Conjunto de vértices que son puntos de articulación
    """
    # Estructura para almacenar todos los datos del algoritmo
    data = {
        "graph": g,  # El grafo original
        "visited": {},  # Diccionario de nodos visitados ("NOT_VISITED" o "VISITED")
        "d": {},  # Tiempo de descubrimiento (depth) de cada nodo
        "low": {},  # Valor 'low' de cada nodo (mínimo tiempo accesible)
        "time": 0,  # Contador global de tiempo para el DFS
        "artic": set(),  # Conjunto de puntos de articulación encontrados
        "parent": {},  # Padre de cada nodo en el árbol DFS
    }

    # Inicialización de estructuras para todos los nodos
    for node in g.keys():
        data["visited"][node] = "NOT_VISITED"
        data["d"][node] = 0
        data["low"][node] = 0
        data["parent"][node] = None

    # Procesamiento DFS para cada componente conexa
    for node in g.keys():
        if data["visited"][node] == "NOT_VISITED":
            dfs_articulation(data, node, True)  # True indica que es la raíz del DFS

    return data["artic"]


def dfs_articulation(data, u, is_root):
    """
    Función recursiva de DFS que calcula los puntos de articulación.

    Args:
        data (dict): Estructura de datos compartida del algoritmo
        u: Nodo actual siendo visitado
        is_root (bool): Indica si este nodo es la raíz del árbol DFS
    """
    # Marcamos el nodo como visitado y establecemos tiempos de descubrimiento
    data["visited"][u] = "VISITED"
    data["time"] += 1
    data["d"][u] = data["low"][u] = data["time"]
    children = 0  # Contador de hijos en el árbol DFS

    # Exploramos todos los vecinos del nodo actual
    for v in data["graph"][u]:
        if data["visited"][v] == "NOT_VISITED":
            # El vecino no ha sido visitado -> es un hijo en el árbol DFS
            data["parent"][v] = u
            children += 1
            dfs_articulation(data, v, False)  # Procesar recursivamente

            # Actualizar el valor low del nodo padre
            data["low"][u] = min(data["low"][u], data["low"][v])

            # Condiciones para punto de articulación:
            # 1. Si es raíz y tiene más de un hijo
            if is_root and children > 1:
                data["artic"].add(u)
            # 2. Si no es raíz y algún hijo no tiene back-edge a ancestros
            if not is_root and data["low"][v] >= data["d"][u]:
                data["artic"].add(u)

        elif v != data["parent"][u]:  # Back-edge (arista a un ancestro ya visitado)
            data["low"][u] = min(data["low"][u], data["d"][v])


# Grafo de prueba (puente)
graph_puente = {
    'A': ['B', 'C'],  # A conectado con B y C
    'B': ['A', 'C'],  # B conectado con A y C
    'C': ['A', 'B', 'D'],  # C conectado con A, B y D (punto de articulación)
    'D': ['C', 'E'],  # D conectado con C y E (punto de articulación)
    'E': ['D']  # E solo conectado con D
}

# Ejecución del algoritmo
print("Puntos de articulación en el grafo puente:", find_articulation_points(graph_puente))
# Salida esperada: {'C', 'D'} (los nodos que al eliminarlos desconectan el grafo)