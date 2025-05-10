from collections import deque

def bfs(g):
    """
    Realiza un recorrido BFS en el grafo `g` para contar el número de componentes conexas.
    Retorna el número de componentes conexas.
    """
    n = len(g)  # Número de nodos en el grafo
    visited = [False] * n  # Lista para marcar los nodos visitados
    ncc = 0  # Contador de componentes conexas

    # Recorremos todos los nodos del grafo
    for v in range(n):
        # Si el nodo no ha sido visitado, es el inicio de una nueva componente conexa
        if not visited[v]:
            ncc += 1  # Incrementamos el contador de componentes conexas
            bfs_aux(g, v, visited)  # Llamamos a BFS para explorar la componente conexa

    return ncc  # Retornamos el número de componentes conexas

def bfs_aux(g, v, visited):
    """
    Realiza un recorrido BFS desde el nodo `v` para explorar su componente conexa.
    Marca todos los nodos alcanzables desde `v` como visitados.
    """
    q = deque()  # Cola para manejar los nodos a visitar
    visited[v] = True  # Marcamos el nodo inicial como visitado
    q.append(v)  # Añadimos el nodo inicial a la cola

    # Mientras haya nodos en la cola
    while q:
        aux = q.popleft()  # Extraemos el nodo actual de la cola
        # Recorremos todos los nodos adyacentes al nodo actual
        for adj in g[aux]:
            # Si el nodo adyacente no ha sido visitado
            if not visited[adj]:
                q.append(adj)  # Lo añadimos a la cola para visitar sus adyacentes
                visited[adj] = True  # Lo marcamos como visitado

# Entrada de nodos y aristas
N, M = map(int, input().strip().split())  # Leemos N (número de pilotes) y M (número de pares de pilotes sin patatas)

# Construcción del grafo como lista de adyacencia
g = [[] for _ in range(N)]  # Inicializamos el grafo con listas vacías

# Leemos las M relaciones de pilotes sin patatas en medio
for _ in range(M):
    u, v = map(int, input().strip().split())  # Leemos una relación u <-> v (grafo no dirigido)
    g[u].append(v)  # Añadimos v a la lista de adyacentes de u
    g[v].append(u)  # Añadimos u a la lista de adyacentes de v (grafo no dirigido)

# Ejecutar BFS para contar componentes conexas
ncc = bfs(g)  # ncc = número de componentes conexas

# Imprimir el número de cucharadas necesarias (una por componente conexa)
print(ncc)
