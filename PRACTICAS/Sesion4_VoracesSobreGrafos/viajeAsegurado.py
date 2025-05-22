# =================================================================
# ALGORITMO Dijkstra PARA "VIAJE ASEGURADO" (SIN heapq)
# Objetivo: Encontrar el maná mínimo (diámetro) para poder teletransportarse
#           entre cualquier pareja de hogueras.
# Complejidad: O(N·(N + M)) para N ≤ 100, M ≤ 2000
# =================================================================

def select_min(distances, visited):
    """
    Selecciona el nodo no visitado con menor distancia actual.
    distances: lista de distancias (1-indexada)
    visited:    lista booleana de nodos ya procesados
    devuelve:   índice del siguiente nodo a procesar
    """
    min_dist = float('inf')
    next_node = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next_node = i
    return next_node


def dijkstra(g, start):
    """
    Calcula distancias mínimas desde 'start' a todos los demás nodos
    usando Dijkstra sin heapq.
    g: lista de adyacencia 1-indexada, g[u] = [(u, v, peso), ...]
    start: nodo inicial (1-indexado)
    retorna: lista de distancias (1-indexada)
    """
    n = len(g) - 1
    distances = [float('inf')] * (n + 1)
    visited   = [False] * (n + 1)

    # inicialización
    distances[start] = 0
    visited[start]   = True
    for _, v, w in g[start]:
        distances[v] = w

    # iterar para los otros n-1 nodos
    for _ in range(2, n + 1):
        u = select_min(distances, visited)
        visited[u] = True
        for _, v, w in g[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances

# ===========================
# LECTURA DE ENTRADA
# ===========================
import sys
input_data = sys.stdin.read().split()
it = iter(input_data)

N = int(next(it))  # número de hogueras
M = int(next(it))  # número de conexiones

# construimos grafo 1-indexado
g = [[] for _ in range(N + 1)]
for _ in range(M):
    h1 = int(next(it)) + 1
    h2 = int(next(it)) + 1
    d  = int(next(it))
    g[h1].append((h1, h2, d))
    g[h2].append((h2, h1, d))

# ===========================
# CÁLCULO DEL DIÁMETRO
# ===========================
max_mana = 0
for start in range(1, N + 1):
    dist = dijkstra(g, start)
    for d in dist[1:]:
        if d != float('inf') and d > max_mana:
            max_mana = d

# ===========================
# SALIDA
# ===========================
print(max_mana)
