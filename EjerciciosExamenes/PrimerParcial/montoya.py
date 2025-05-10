from collections import deque

def bfs(g, start, end, maximo):
    n = len(g)
    visited = [False] * n
    q = deque()
    q.append((start, 0))  # (nodo, número de pasos)
    visited[start] = True

    while q:
        aux, steps = q.popleft()

        # Si hemos llegado al nodo de destino, revisamos si se cumple la condición
        if aux == end:
            if steps <= maximo:
                print(steps + 1)  # Sumamos 1 para contar el nodo final también
            else:
                print("MON TOYA POR FAVOR")
            return

        # Expandimos los vecinos
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append((adj, steps + 1))

    # Si no se ha encontrado un camino hasta el final
    print("MONTOYA POR FAVOR")


# N = NODOS, Numero de puntos de control que hay
# M = ARISTAS, Numero de caminos que conectan directamente puntos de control
# C = Numero de casos que vamos a probar

N, M, C = map(int, input().strip().split())

g = [[] for _ in range(N)]  # Lista de adyacencia

# Leemos las aristas
for _ in range(M):
    U, V = map(int, input().strip().split())
    g[U].append(V)
    g[V].append(U)

# Procesamos los casos
for _ in range(C):
    O, D, P = map(int, input().strip().split())
    bfs(g, O, D, P)
