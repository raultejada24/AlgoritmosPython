from collections import deque

def bfs(g, M):
    """
    Realiza una BFS limitada hasta el nivel M-1 desde el nodo 0.
    Retorna el número de nodos alcanzables.
    """
    n = len(g)
    visited = [False] * n
    count = 0
    q = deque()

    # Inicialización para el nodo 0 (nivel 0)
    visited[0] = True
    count += 1
    q.append((0, 0))  # (nodo, nivel)

    while q:
        node, level = q.popleft()

        # Solo procesamos si no hemos alcanzado el nivel máximo
        if level >= M - 1:
            for adj in g[node]:
                if not visited[adj]:
                    visited[adj] = True
                    count += 1
                    q.append((adj, level + 1))

    return count


# Entrada principal
N = int(input())

for _ in range(N):
    M, K, C = map(int, input().split())
    g = [[] for _ in range(K)]  # Lista de adyacencia

    for _ in range(C):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)  # Grafo no dirigido

    print(bfs(g, M))
