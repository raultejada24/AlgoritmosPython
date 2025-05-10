# =================================================================
# ALGORITMO DE KRUSKAL PARA "ATAQUE DE LOS TITANES"
# Objetivo: Conectar todos los puestos seguros con el mínimo cable (cada 5m = 1€)
# =================================================================

# Función para extraer y ordenar aristas por distancia (ascendente)
def sort_candidates(graph):
    candidates = []
    for adjs in graph:  # Recorrer lista de adyacencia
        for (src, dst, weight) in adjs:
            candidates.append((weight, src, dst))  # Guardar como (distancia, origen, destino)
    candidates.sort()  # Ordenar por distancia
    return candidates

# Función para unir componentes en el Union-Find
def update_components(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

# Algoritmo de Kruskal adaptado
def kruskal(graph):
    candidates = sort_candidates(graph)  # Aristas ordenadas
    components = list(range(len(graph)))  # Cada nodo es su propio componente
    total_distance = 0
    num_components = len(graph)

    i = 0
    while i < len(candidates) and num_components > 1:
        weight, src, dst = candidates[i]
        if components[src] != components[dst]:  # Si no están conectados
            total_distance += weight
            num_components -= 1
            update_components(components, components[src], components[dst])
        i += 1

    return (total_distance + 4) // 5  # Redondeo hacia arriba cada 5m

# --- LECTURA DE ENTRADA DIRECTA ---
# Leer N (puestos) y M (conexiones)
N, M = map(int, input().strip().split())

# Inicializar grafo
graph = [[] for _ in range(N)]

# Leer conexiones (grafo no dirigido)
for _ in range(M):
    n1, n2, d = map(int, input().strip().split())
    graph[n1].append((n1, n2, d))  # Arista en una dirección
    graph[n2].append((n2, n1, d))  # Arista inversa

# Calcular e imprimir costo mínimo
print(kruskal(graph))

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. sort_candidates(): Ordena aristas para procesar las más cortas primero
# 2. update_components(): Une grupos de nodos durante el MST
# 3. (total_distance + 4) // 5: Fórmula mágica para redondear al múltiplo de 5 superior
# =================================================================