def select_min(distances, visited):
    """Selecciona el nodo no visitado con menor distancia actual"""
    min_dist = float('inf')
    next_node = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next_node = i
    return next_node


def dijkstra(g, start):
    """Calcula las distancias mínimas desde el nodo inicial a todos los demás"""
    n = len(g) - 1  # Los nodos empiezan en 1
    distances = [float('inf')] * (n + 1)  # Distancias iniciales (infinito)
    visited = [False] * (n + 1)  # Nodos visitados

    distances[start] = 0  # La distancia al nodo inicial es 0
    visited[start] = True

    # Inicializa distancias de los nodos adyacentes al inicio
    for u, v, w in g[start]:
        distances[v] = w

    # Itera n-1 veces (para todos los nodos restantes)
    for _ in range(2, n + 1):
        next_node = select_min(distances, visited)  # Selecciona el nodo más cercano
        visited[next_node] = True

        # Actualiza distancias de los vecinos del nodo seleccionado
        for u, v, w in g[next_node]:
            distances[v] = min(distances[v], distances[u] + w)

    return distances


# Grafo representado como lista de adyacencia (nodos indexados desde 1)
# Formato: (origen, destino, peso)
g = [
    [],  # Nodo 0 no usado
    [(1, 2, 5), (1, 4, 3)],  # Conexiones nodo 1
    [(2, 5, 1)],  # Conexiones nodo 2
    [],  # Nodo 3 sin conexiones salientes
    [(4, 2, 1), (4, 3, 11), (4, 5, 6)],  # Conexiones nodo 4
    [(5, 3, 1)]  # Conexiones nodo 5
]

start = 1
sol = dijkstra(g, start)
print(sol)  # Output: [inf, 0, 4, 12, 3, 5]