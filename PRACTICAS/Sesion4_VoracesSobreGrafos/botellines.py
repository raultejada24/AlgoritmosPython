# =================================================================
# ALGORITMO DE DIJKSTRA PARA "BOTELLINES"
# Objetivo: Encontrar el camino mínimo entre dos cervezas específicas (nodos S y E)
# Complejidad: O(N^2) por el select_min (óptimo para N ≤ 1000)
# =================================================================

def select_min(distances, visited):
    """Selecciona el nodo no visitado con menor distancia actual"""
    min_dist = float('inf')
    next_node = None
    for node in range(len(distances)):
        if not visited[node] and distances[node] < min_dist:
            min_dist = distances[node]
            next_node = node
    return next_node


def dijkstra(g, start, end):
    """Calcula el camino mínimo desde 'start' hasta 'end'
       Retorna: (distancia_total, camino)"""
    n = len(g)
    distances = [float('inf')] * n  # Distancias iniciales
    visited = [False] * n  # Nodos visitados
    previous = [-1] * n  # Para reconstruir el camino

    distances[start] = 0  # Distancia al nodo inicial es 0

    for _ in range(n):
        u = select_min(distances, visited)  # Nodo más cercano no visitado
        if u == end:  # Llegamos al destino
            break
        if u is None:  # No hay camino
            return float('inf'), []

        visited[u] = True

        # Actualizar distancias de vecinos
        for edge in g[u]:
            v, w = edge[1], edge[2]
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                previous[v] = u

    # Reconstruir camino
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = previous[node]
    path.reverse()

    return distances[end], path


# =================================================================
# LECTURA DE ENTRADA Y EJECUCIÓN
# =================================================================

# Leer número de cervezas (N) y conexiones (M)
N, M = map(int, input().strip().split())

# Construir grafo (lista de adyacencia)
g = [[] for _ in range(N)]
for _ in range(M):
    C1, C2, D = map(int, input().strip().split())
    g[C1].append((C1, C2, D))  # Conexión en ambas direcciones
    g[C2].append((C2, C1, D))

# Leer cervezas de inicio (S) y fin (E)
S, E = map(int, input().strip().split())

# Calcular y mostrar resultados
distance, path = dijkstra(g, S, E)
print(distance)
print(' '.join(map(str, path)))

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. select_min(): Encuentra el nodo no visitado más cercano (O(N))
# 2. previous[]: Reconstruye el camino desde E hasta S
# 3. Parada temprana: Termina al llegar al nodo destino
# 4. Grafo no dirigido: Conexiones añadidas en ambas direcciones
# =================================================================
# ¿POR QUÉ DIJKSTRA?
# - Requerimiento: Camino mínimo entre DOS nodos específicos
# - Características: Pesos no negativos (D ≥ 1) si no sería un BFS
# - Necesidad: Mostrar distancia y camino exacto
# =================================================================