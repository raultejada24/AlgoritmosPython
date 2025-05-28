## Depth First Search (DFS) - Búsqueda en Profundidad
## Explora profundamente, útil para detectar ciclos o para recorrer grafos en profundidad.

def dfs(g):
    n = len(g) - 1  # Número de nodos en el grafo (restamos 1 porque la lista tiene una posición vacía al inicio)
    visited = set()  # Usamos un conjunto para almacenar los nodos visitados (es más eficiente que una lista para esta operación)
    # Alternativamente, podríamos usar una lista de booleanos: visited = [False] * (n + 1)

    # Recorremos todos los nodos del grafo
    for v in range(1, n + 1):  # Empezamos desde el nodo 1 hasta el nodo n
        if v not in visited:  # Si el nodo no ha sido visitado
            # Llamamos a la función recursiva para procesar el nodo y sus adyacentes
            dfs_rec(g, v, visited)


## Función recursiva de DFS
def dfs_rec(g, v, visited):
    visited.add(v)  # Marcamos el nodo actual como visitado (lo añadimos al conjunto)
    print(v, end=" ")  # Imprimimos el nodo actual

    # Recorremos todos los nodos adyacentes al nodo actual
    for adj in g[v]:  # g[v] es la lista de nodos adyacentes al nodo v
        if adj not in visited:  # Si el nodo adyacente no ha sido visitado
            dfs_rec(g, adj, visited)  # Llamada recursiva para procesar el nodo adyacente


# Representación del grafo como una lista de listas de adyacencia
# Por ejemplo, los adyacentes del nodo 3 son g[3] --> [2, 4, 5]
# El primer adyacente del nodo 3 es g[3][0] --> 2

# Ejemplo: Imprimir los adyacentes del nodo 3
# print(g[3])  # Salida: [2, 4, 5]

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

dfs(g)