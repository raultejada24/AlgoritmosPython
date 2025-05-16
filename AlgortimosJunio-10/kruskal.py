# Árbol de recubrimiento
# Complejidad O(n^2)
def sort_candidates(graph):
    """Extrae y ordena aristas por peso (ascendente)"""
    candidates = []
    for adjs in graph:
        for (src, dst, weight) in adjs:
            candidates.append((weight, src, dst))
    candidates.sort()
    return candidates


def update_components(components, new_id, old_id):
    """Unifica componentes conexos"""
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(graph):
    """Implementación clásica de Kruskal para MST"""
    candidates = sort_candidates(graph)
    components = list(range(len(graph)))  # Inicialmente cada nodo es su propio componente
    solution = 0

    i = 0
    num_components = len(graph)
    while i < len(candidates) and num_components > 1:
        weight, src, dst = candidates[i]

        # Verifica si la arista conecta componentes distintos
        if components[src] != components[dst]:
            solution += weight
            num_components -= 1
            update_components(components, components[src], components[dst])

        i += 1

    return solution


# Grafo no dirigido (aristas duplicadas 1-3 y 3-1)
graph = [
    [],  # Nodo 0 dummy
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
]

print(kruskal(graph))  # Output correcto: 15