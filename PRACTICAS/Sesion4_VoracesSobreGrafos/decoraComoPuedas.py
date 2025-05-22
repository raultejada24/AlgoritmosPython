def select_min(distances, visited):
    """
    Similar a getBestItem: selecciona el índice del nodo no visitado
    con menor distancia actual.
    """
    min_dist = float('inf')
    next_node = None
    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next_node = i
    return next_node

def dijkstra(g, start):
    """
    Dijkstra iterativo sin heapq, partiendo del nodo `start`.
    g: lista de adyacencia 0-indexada, g[u] = [(v, peso), ...]
    devuelve: lista `distances` con la distancia mínima desde `start` a cada nodo
    """
    n = len(g)
    distances = [float('inf')] * n
    visited   = [False] * n

    # Inicialización
    distances[start] = 0
    visited[start]   = True
    # Establece distancias directas desde el inicio
    for v, w in g[start]:
        distances[v] = w

    # Procesar los otros n-1 nodos
    for _ in range(1, n):
        u = select_min(distances, visited)
        if u is None:
            break
        visited[u] = True
        # Relajar aristas salientes de u
        for v, w in g[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances

# --- Lectura de entrada ---
n, m, T = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, input().split())
    g[u].append((v, d))
    g[v].append((u, d))

# --- Cálculo de tiempos mínimos desde el sofá (nodo 0) ---
distances = dijkstra(g, 0)

# Suma total de los tiempos de ida a cada habitación
total_time = sum(distances)

# --- Salida según pueda o no decorar a tiempo ---
if total_time <= T:
    print(total_time)
else:
    print("Aleg, ¡a decorar!")
