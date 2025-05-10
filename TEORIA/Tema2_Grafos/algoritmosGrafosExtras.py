
from collections import deque

# Comprobar si un grafo es bipartito
def es_bipartito(g):
    color = {}

    # Recorremos todos los nodos del grafo
    for nodo in g:
        if nodo not in color:
            # Usamos BFS para intentar colorear el grafo
            if not bfs_bipartito(g, nodo, color):
                return False
    return True

def bfs_bipartito(g, nodo, color):
    cola = deque([nodo])
    color[nodo] = 0  # Empezamos coloreando el nodo con color 0

    while cola:
        u = cola.popleft()
        for v in g[u]:
            if v not in color:
                color[v] = 1 - color[u]  # Coloreamos con el color opuesto
                cola.append(v)
            elif color[v] == color[u]:
                return False  # Si encontramos un conflicto, no es bipartito
    return True


# Detectar ciclos en un grafo
def detectar_ciclo(g):
    visited = set()
    rec_stack = set()

    # Recorremos todos los nodos
    for nodo in g:
        if nodo not in visited:
            if dfs_ciclo(g, nodo, visited, rec_stack):
                return True
    return False

def dfs_ciclo(g, nodo, visited, rec_stack):
    visited.add(nodo)
    rec_stack.add(nodo)

    for vecino in g[nodo]:
        if vecino not in visited:
            if dfs_ciclo(g, vecino, visited, rec_stack):
                return True
        elif vecino in rec_stack:
            return True

    rec_stack.remove(nodo)
    return False


# Camino más largo en un DAG
def camino_mas_largo_dag(g):
    top_order = top_sort(g)
    dist = {nodo: float('-inf') for nodo in g}
    dist[top_order[0]] = 0  # El primer nodo tiene distancia 0

    # Relajación de las aristas siguiendo el orden topológico
    for nodo in top_order:
        for vecino in g[nodo]:
            if dist[vecino] < dist[nodo] + 1:
                dist[vecino] = dist[nodo] + 1

    return dist


# Orden topológico para el DAG
def top_sort(g):
    visited = set()
    order = []

    def dfs(nodo):
        visited.add(nodo)
        for vecino in g[nodo]:
            if vecino not in visited:
                dfs(vecino)
        order.append(nodo)

    for nodo in g:
        if nodo not in visited:
            dfs(nodo)

    return order[::-1]


# Detectar si dos nodos están conectados
def estan_conectados(g, nodo1, nodo2):
    visited = set()

    def dfs(nodo):
        if nodo == nodo2:
            return True
        visited.add(nodo)
        for vecino in g[nodo]:
            if vecino not in visited:
                if dfs(vecino):
                    return True
        return False

    return dfs(nodo1)


# Caminos y ciclos eulerianos
def tiene_ciclo_euleriano(g):
    # Un grafo tiene un ciclo euleriano si todos sus vértices tienen grado par
    for nodo in g:
        if len(g[nodo]) % 2 != 0:
            return False
    return True

def tiene_camino_euleriano(g):
    # Un grafo tiene un camino euleriano si tiene exactamente 0 o 2 vértices con grado impar
    odd_count = 0
    for nodo in g:
        if len(g[nodo]) % 2 != 0:
            odd_count += 1
    return odd_count == 0 or odd_count == 2


# Cierre transitivo
def cierre_transitivo(g):
    closure = {nodo: set(g[nodo]) for nodo in g}

    for k in g:
        for i in g:
            for j in g:
                if i in closure[k] and j in closure[k]:
                    closure[i].add(j)

    return closure


# Caminos entre un origen y un destino con k aristas
def caminos_k_aristas(g, origen, destino, k):
    caminos = []

    def dfs_camino(nodo, camino):
        if len(camino) == k:
            if nodo == destino:
                caminos.append(camino[:])
            return

        for vecino in g[nodo]:
            dfs_camino(vecino, camino + [vecino])

    dfs_camino(origen, [origen])
    return caminos


## Datos (Representación del grafo como diccionario de listas de adyacencia)
g = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

# Comprobar si el grafo es bipartito
print("Es bipartito:", es_bipartito(g))

# Detectar ciclos en el grafo
print("Tiene ciclo:", detectar_ciclo(g))

# Camino más largo en un DAG
g_dag = {
    0: [1],
    1: [2],
    2: [3],
    3: []
}
print("Camino más largo en el DAG:", camino_mas_largo_dag(g_dag))

# Ver si dos nodos están conectados
print("Están conectados 0 y 4:", estan_conectados(g, 0, 4))

# Comprobar caminos y ciclos eulerianos
print("Tiene ciclo euleriano:", tiene_ciclo_euleriano(g))
print("Tiene camino euleriano:", tiene_camino_euleriano(g))

# Cierre transitivo
print("Cierre transitivo del grafo:", cierre_transitivo(g))

# Caminos con k aristas
print("Caminos con 2 aristas entre 0 y 4:", caminos_k_aristas(g, 0, 4, 2))
