from collections import deque


def bfs(g, start):
    n = len(g)
    visited = [False] * n
    q = deque()

    def bfs_aux(v):
        visited[v] = True
        q.append(v)
        count = 1

        while q:
            aux = q.popleft()
            for adj in g[aux]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append(adj)
                    count += 1
        return count

    return bfs_aux(start)


# Entrada principal
N, M = map(int, input().strip().split())
g = {i: [] for i in range(N)}

for _ in range(M):
    x, y = map(int, input().strip().split())
    g[x].append(y)

# Convertir diccionario a lista de adyacencia
graph_list = [g[i] for i in range(N)]

# Ejecutar BFS desde el nodo 0
nodos_visitados = bfs(graph_list, 0)

# Verificación de conexión
if nodos_visitados == N:
    print("CASTING COMPLETO")
else:
    print("HAY QUE REPETIR")