def encontrar_puntos_articulacion(grafo, n, costes):
    """
    Encuentra los nodos críticos (puntos de articulación) en el grafo y suma sus costes.
    """
    # Usamos una lista de un elemento para el tiempo (objeto mutable)
    tiempo = [0]  # tiempo[0] actuará como contador
    visitado = [False] * n
    disc = [float("inf")] * n
    low = [float("inf")] * n
    parent = [-1] * n
    articulaciones = set()

    def dfs(u):
        children = 0
        visitado[u] = True
        disc[u] = low[u] = tiempo[0]
        tiempo[0] += 1  # Modificamos el contenido de la lista (no reasignamos)

        for v in grafo[u]:
            if not visitado[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    articulaciones.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    articulaciones.add(u)

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visitado[i]:
            dfs(i)

    return sum(costes[u] for u in articulaciones)


n, m = map(int, input().split())
costes = [int(input()) for _ in range(n)]

grafo = {i: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

print(encontrar_puntos_articulacion(grafo, n, costes))