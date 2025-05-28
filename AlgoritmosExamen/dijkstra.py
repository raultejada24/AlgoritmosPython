def select_min(distances, visited): # Parecida a getBestItem
    min_dist = float('inf')
    next_node = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next_node = i
    return next_node


def dijkstra(g, start):
    n = len(g) - 1
    distances = [float('inf')] * (n + 1)  # Distancias iniciales (infinito)
    visited = [False] * (n + 1)

    distances[start] = 0  # La distancia al nodo inicial es 0
    visited[start] = True

    # Inicializa distancias de los nodos adyacentes al inicio
    for _, destino, peso in g[start]:
        distances[destino] = peso

    # Itera n-1 veces (para todos los nodos restantes)
    for _ in range(2, n + 1): # Empieza en 2 siempre
        next_node = select_min(distances, visited)  # Selecciona nodo más cercano
        visited[next_node] = True

        # Actualiza distancias de los vecinos del nodo seleccionado
        for _, destino, peso in g[next_node]:
            distances[destino] = min(distances[destino], distances[next_node] + peso)

    return distances


# Lista de adyacencia (nodos indexados desde 1)
# Formato: (origen, destino, peso)
g = [
    [],  # Nodo 0 no usado
    [(1, 2, 5), (1, 4, 3)],  # Conexiones salientes nodo 1
    [(2, 5, 1)],
    [],  # Nodo 3 sin conexiones salientes
    [(4, 2, 1), (4, 3, 11), (4, 5, 6)],  # Conexiones salientes nodo 4
    [(5, 3, 1)]
]

start = 1
sol = dijkstra(g, start)
print(sol)