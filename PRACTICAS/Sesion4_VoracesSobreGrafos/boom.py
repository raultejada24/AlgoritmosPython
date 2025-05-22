# =================================================================
# ALGORITMO PARA "¡¡¡BOOM!!!" (Sin heapq ni sys)
# Objetivo: Para cada tipo de componente, calcular la mínima longitud
# de cable necesaria para conectar dos componentes del mismo tipo.
# Complejidad: O(T · (N·(N + M))) con Dijkstra iterativo por tipo
# =================================================================

def select_min(distances, visited):
    """
    Selecciona el índice del nodo no visitado con menor distancia.
    distances: lista de distancias actuales
    visited:    lista booleana marcando nodos ya procesados
    devuelve:   índice del nodo con distancia mínima
    """
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
    sin estructuras avanzadas (sin heapq).
    graph: lista de adyacencia, donde graph[u] = [(v, peso), ...]
    start: nodo inicial (0-indexado)
    devuelve: lista de distancias mínimas a cada nodo
    """
    n = len(graph)
    distances = [float('inf')] * n
    visited   = [False] * n

    # 1) Inicialización
    distances[start] = 0

    # 2) Repetir N veces: seleccionar y relajar
    for _ in range(n):
        u = select_min(distances, visited)
        if u == -1:               # todos los alcanzables procesados
            break
        visited[u] = True
        # Relajación de aristas salientes de u
        for v, w in graph[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances


# =================================================================
# LECTURA DE ENTRADA
# =================================================================
# N: número de componentes, M: número de conexiones
N, M = map(int, input().split())
# Tipo de cada componente (0-indexado, valores arbitrarios)
types = list(map(int, input().split()))

# Grafo no dirigido en lista de adyacencia
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


# =================================================================
# AGRUPACIÓN DE NODOS POR TIPO
# =================================================================
# type_dict[t] = lista de nodos que son del tipo t
type_dict = {}
for node, t in enumerate(types):
    type_dict.setdefault(t, []).append(node)


# =================================================================
# CÁLCULO DE LONGITUD MÍNIMA POR TIPO
# =================================================================
results = []
# Iteramos en orden creciente de tipo
for t in sorted(type_dict):
    nodes = type_dict[t]
    # Si hay menos de dos nodos, no hay cable que tender → 0
    if len(nodes) < 2:
        results.append(0)
        continue

    min_len = float('inf')
    # Para cada nodo del tipo, hacemos Dijkstra y comprobamos pares
    for i in range(len(nodes)):
        dist = dijkstra(graph, nodes[i])
        # Comparamos con los que vengan después
        for j in range(i + 1, len(nodes)):
            target = nodes[j]
            if dist[target] < min_len:
                min_len = dist[target]

    # Si nunca se conectaron, min_len quedaría infinito; asumimos 0
    results.append(min_len if min_len != float('inf') else 0)


# =================================================================
# SALIDA
# =================================================================
# Imprimimos, para cada tipo en orden, la mínima longitud de cable
print(' '.join(map(str, results)))

