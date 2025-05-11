# =================================================================
# ALGORITMO dijkstra PARA "VIAJE ASEGURADO"
# Objetivo: Encontrar el maná mínimo para viajar entre cualquier par de hogueras
#           minimizando la mayor distancia entre parejas (diámetro del grafo)
# Complejidad: O(N·(N+M)) para N ≤ 100, M ≤ 2000
# =================================================================

import sys

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
    visited = [False] * (n + 1)           # Nodos visitados

    distances[start] = 0
    visited[start] = True

    # Inicializa distancias de los nodos adyacentes al inicio
    for u, v, w in g[start]:
        distances[v] = w

    # Itera n-1 veces (para todos los nodos restantes)
    for _ in range(2, n + 1):
        u = select_min(distances, visited)
        visited[u] = True
        # Actualiza distancias de los vecinos del nodo seleccionado
        for _, v, w in g[u]:
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances  # solo necesitamos las distancias

# =================================================================
# LECTURA DE ENTRADA Y EJECUCIÓN
# =================================================================

# Leer número de hogueras (N) y conexiones (M)
N, M = map(int, sys.stdin.readline().split())

# Construir grafo 1-indexado para Dijkstra
g = [[] for _ in range(N + 1)]
for _ in range(M):
    H1, H2, D = map(int, sys.stdin.readline().split())
    # ajustar a 1-indexado
    H1 += 1
    H2 += 1
    g[H1].append((H1, H2, D))
    g[H2].append((H2, H1, D))

# Para cada hoguera, calculamos distancias mínimas y recogemos la máxima
max_mana = 0
for start in range(1, N + 1):
    distances = dijkstra(g, start)
    # actualizamos el maná necesario como la mayor distancia encontrada
    for d in distances[1:]:
        if d != float('inf') and d > max_mana:
            max_mana = d

# Mostrar resultado: maná mínimo requerido (diámetro del grafo)
print(max_mana)

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. dijkstra/select_min: obtenemos distancias cortas desde cada hoguera
# 2. El maná requerido es la distancia máxima en todas las parejas
# 3. O(N·(N+M)) suficiente para N ≤ 100, M ≤ 2000
# =================================================================

