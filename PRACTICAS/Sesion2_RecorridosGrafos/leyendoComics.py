from collections import deque

# Inicializar estructuras
visitado = [False] * N
orden = deque()

# Función DFS
def dfs(nodo):
    visitado[nodo] = True
    for vecino in grafo[nodo]:
        if not visitado[vecino]:
            dfs(vecino)
    orden.appendleft(nodo)

# Aplicar DFS
for i in range(N):
    if not visitado[i]:
        dfs(i)

# Leer entrada
N, M = map(int, input().split())

# Construir grafo
grafo = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    grafo[A].append(B)

# Mostrar resultado
print(' '.join(map(str, orden)))