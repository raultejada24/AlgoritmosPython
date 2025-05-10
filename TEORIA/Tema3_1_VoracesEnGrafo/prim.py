import random


def select_min(candidates, visited):
    """Selecciona el nodo no visitado con menor distancia"""
    node = None
    weight = float('inf')
    for i in range(1, len(candidates)):  # Empieza en 1 porque el nodo 0 no se usa
        if not visited[i] and candidates[i] < weight:
            node = i
            weight = candidates[i]
    return node, weight


def prim(g):
    """Algoritmo de Prim para MST - Versión con error conocido"""
    n = len(g)
    initial = random.randint(1, n - 1)  # Elige nodo inicial aleatorio (entre 1 y n-1)
    sol = 0
    visited = [False] * n
    candidates = [float("inf")] * n  # Inicializa todas las distancias a infinito

    # Inicializa distancias para nodos adyacentes al inicial
    for (start, end, weight) in g[initial]:
        candidates[end] = weight  # Actualiza distancia a nodos vecinos

    visited[initial] = True

    for _ in range(2, n):  # Necesitamos n-1 aristas
        next_node, cost = select_min(candidates, visited)
        if cost < float("inf"):
            visited[next_node] = True
            sol += cost
            # Actualiza distancias para nodos adyacentes al nuevo nodo
            for (start, end, weight) in g[next_node]:
                if not visited[end]:
                    candidates[end] = min(candidates[end], weight)
    return sol


grafo = [
    [],
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],  # (origen, destino, peso)
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
]

print(prim(grafo))  # Debería dar 15