# =================================================================
# ALGORITMO DE DIJKSTRA PARA "BOTELLINES"
# Objetivo: Encontrar el camino mínimo entre dos cervezas específicas (nodos S y E)
# Complejidad: O(N^2) por el select_min (óptimo para N ≤ 1000)
# =================================================================

def select_min(distances, visited):
    """
    Selecciona el nodo no visitado con menor distancia actual.
    distances: lista de distancias actuales
    visited:    lista booleana marcando nodos ya procesados
    devuelve:   índice del nodo con distancia mínima (o None si todos visitados)
    """
    min_dist = float('inf')
    next_node = None
    for i, d in enumerate(distances):
        if not visited[i] and d < min_dist:
            min_dist = d
            next_node = i
    return next_node


def dijkstra(g, start, end):
    """
    Calcula el camino mínimo desde 'start' hasta 'end' sin usar heapq.
    g:    lista de adyacencia, donde g[u] = [(v, peso), ...]
    start,end: índices de vértices (0-indexado)
    retorna: (distancia_total, camino_completo_como_lista)
    """
    n = len(g)
    distances = [float('inf')] * n
    visited   = [False] * n
    previous  = [-1] * n

    distances[start] = 0

    for _ in range(n):
        u = select_min(distances, visited)
        if u is None or distances[u] == float('inf'):
            break
        if u == end:
            break
        visited[u] = True

        # Relajar cada arista (u -> v) de peso w
        for v, w in g[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous[v] = u

    # Reconstrucción de la ruta de end a start
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = previous[cur]
    path.reverse()

    return distances[end], path


# =================================================================
# LECTURA DE ENTRADA
# =================================================================
# N: número de cervezas (nodos), M: número de conexiones (aristas)
N, M = map(int, input().split())

# Construir grafo no dirigido
g = [[] for _ in range(N)]
for _ in range(M):
    C1, C2, D = map(int, input().split())
    g[C1].append((C2, D))
    g[C2].append((C1, D))

# Nodos de inicio y fin
S, E = map(int, input().split())

# =================================================================
# EJECUTAR DIJKSTRA Y SALIDA DE RESULTADOS
# =================================================================
distance, path = dijkstra(g, S, E)

# Imprimir distancia y secuencia de nodos recorridos
print(distance)
print(' '.join(map(str, path)))
