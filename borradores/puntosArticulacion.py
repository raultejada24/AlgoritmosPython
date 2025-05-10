def find_articulation_points(g):
    data = {
        "graph": g,
        "visited": {},
        "d": {},
        "low": {},
        "time": 0,
        "artic": set(),
        "parent": {},
    }

    # Inicialización correcta de los diccionarios
    for k in g.keys():
        data["visited"][k] = "NOT_VISITED"
        data["d"][k] = 0
        data["low"][k] = 0
        data["parent"][k] = None

    for k in g.keys():
        if data["visited"][k] == "NOT_VISITED":
            dfs_articulation(data, k, True)  # El primer nodo es raíz

    return data["artic"]

def dfs_articulation(data, u, is_root):
    data["visited"][u] = "VISITED"
    data["time"] += 1
    data["d"][u] = data["low"][u] = data["time"]
    children = 0

    for v in data["graph"][u]:
        if data["visited"][v] == "NOT_VISITED":
            data["parent"][v] = u
            children += 1
            dfs_articulation(data, v, False)

            data["low"][u] = min(data["low"][u], data["low"][v])

            # Condición para punto de articulación
            if is_root and children > 1:
                data["artic"].add(u)
            if not is_root and data["low"][v] >= data["d"][u]:
                data["artic"].add(u)
        elif v != data["parent"][u]:  # Back-edge
            data["low"][u] = min(data["low"][u], data["d"][v])

# Grafo de prueba
graph_puente = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}

print("Puntos de articulación en el grafo puente:", find_articulation_points(graph_puente))