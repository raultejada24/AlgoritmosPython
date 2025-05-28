
## Breadth First Search (BFS) - Búsqueda en Anchura
## Explora por niveles, útil para encontrar el camino más corto en grafos No ponderados.

from collections import deque  # Cola doblemente enlazada

## Implementación Iterativa de BFS
def bfs(g):
    n = len(g) - 1  # Obtenemos el número de nodos en el grafo (restamos 1 porque la lista tiene una posición vacía al inicio)
    visited = [False] * (n + 1)  # Creamos una lista de booleanos para marcar los nodos visitados

    # Recorremos todos los nodos del grafo
    for v in range(1, n):
        if not visited[v]:  # Si el nodo no ha sido visitado, llamamos a la función auxiliar
            bfs_aux(g, v, visited)


def bfs_aux(g, v, visited):
    q = deque()  # Creamos una cola vacía
    visited[v] = True  # Marcamos el nodo actual como visitado
    print(v, end=" ")  # Imprimimos el nodo actual
    q.append(v)  # Añadimos el nodo actual a la cola

    # Mientras la cola no esté vacía
    while q:
        aux = q.popleft()  # Sacamos el primer elemento de la cola (nodo actual)

        # Recorremos todos los nodos adyacentes al nodo actual
        for adj in g[aux]:
            if not visited[adj]:  # Si el nodo adyacente no ha sido visitado
                print(adj, end=" ")  # Imprimimos el nodo adyacente
                visited[adj] = True  # Marcamos el nodo adyacente como visitado
                q.append(adj)  # Añadimos el nodo adyacente a la cola

                # Nota: Si usáramos `appendleft` en lugar de `append`, estaríamos haciendo un recorrido en profundidad iterativo.

## Datos del Grafo
g = [
    [],         # Posición 0 vacía para que los índices coincidan con los números de los nodos
    [2, 4, 8],  # Nodos adyacentes al nodo 1
    [1, 3, 4],  # Nodos adyacentes al nodo 2
    [2, 4, 5],  # Nodos adyacentes al nodo 3
    [1, 2, 3, 7],  # Nodos adyacentes al nodo 4
    [3, 6],     # Nodos adyacentes al nodo 5
    [5, 7],     # Nodos adyacentes al nodo 6
    [4, 6, 9],  # Nodos adyacentes al nodo 7
    [1, 9],     # Nodos adyacentes al nodo 8
    [7, 8]      # Nodos adyacentes al nodo 9
]

## Llamada a la función BFS
bfs(g)