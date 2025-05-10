# =================================================================
# ALGORITMO PARA "¡¡¡BOOM!!!" (Sin heapq ni sys)
# Objetivo: Para cada tipo de componente, calcular la mínima longitud
# de cable necesaria para conectar dos componentes del mismo tipo.
# =================================================================

def select_min(distances, visited):
    """Selecciona el índice del nodo no visitado con menor distancia"""
    min_dist = float('inf')
    min_node = -1
    for idx, d in enumerate(distances):
        if not visited[idx] and d < min_dist:
            min_dist = d
            min_node = idx
    return min_node


def dijkstra(graph, start):
    """
    Calcula distancias mínimas desde 'start' a todos los nodos usando Dijkstra
    sin estructuras avanzadas.
    graph: lista de adyacencia, donde graph[u] = [(v, peso), ...]
    start: nodo inicial (0-indexado)
    devuelve: lista de distancias
    """
    n = len(graph)
    distances = [float('inf')] * n
    visited = [False] * n

    distances[start] = 0
    for _ in range(n):
        u = select_min(distances, visited)
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    return distances

# =================================================================
# LECTURA DE ENTRADA
# =================================================================
N, M = map(int, input().split())  # N: componentes, M: conexiones
types = list(map(int, input().split()))  # Tipo de cada componente (0-indexado)

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# Agrupar nodos por tipo
type_dict = {}
for node, t in enumerate(types):
    type_dict.setdefault(t, []).append(node)

# =================================================================
# CÁLCULO Y SALIDA DE RESULTADOS
# =================================================================
results = []
for t in sorted(type_dict):
    nodes = type_dict[t]
    # Si hay menos de dos nodos, la longitud mínima es 0
    if len(nodes) < 2:
        results.append(0)
    else:
        min_len = float('inf')
        for i in range(len(nodes)):
            dist = dijkstra(graph, nodes[i])
            for j in range(i + 1, len(nodes)):
                target = nodes[j]
                if dist[target] < min_len:
                    min_len = dist[target]
        results.append(min_len)

print(' '.join(map(str, results)))  # Mostrar resultados por tipo

# =================================================================
# FIN DEL ALGORITMO
# =================================================================
