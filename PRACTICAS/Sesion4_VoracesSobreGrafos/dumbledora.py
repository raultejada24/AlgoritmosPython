# =================================================================
# ALGORITMO DE KRUSKAL PARA "Juro solemnemente que esto es una travesura"
# Objetivo: Conectar todas las habitaciones con mínimo coste y calcular costes individuales
# Complejidad: O(M log M) por el ordenamiento (óptimo para M ≤ 200,000)
# =================================================================

def sort_candidates(graph):
    """Extrae y ordena aristas por peso (coste) ascendente"""
    candidates = []
    for adjs in graph:
        for (src, dst, weight) in adjs:
            if src < dst:  # Evitar duplicar aristas (grafo no dirigido)
                candidates.append((weight, src, dst))
    candidates.sort()
    return candidates


# =================================================================
# UNION-FIND OPTIMIZADO CON COMPRESIÓN DE CAMINOS Y UNIÓN POR RANGO
# =================================================================

def find(parent, u):
    """Devuelve el representante del conjunto al que pertenece u"""
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    """Une los conjuntos de u y v y devuelve True si estaban separados"""
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
    return True


# =================================================================
# LECTURA DE ENTRADA Y EJECUCIÓN
# =================================================================

# Leer número de habitaciones (N) y pasillos (M)
N, M = map(int, input().strip().split())

# Construir grafo (lista de adyacencia)
graph = [[] for _ in range(N)]
for _ in range(M):
    H1, H2, C = map(int, input().strip().split())
    graph[H1].append((H1, H2, C))
    graph[H2].append((H2, H1, C))

# Preparar estructuras para Kruskal
candidates = sort_candidates(graph)
parent = list(range(N))
rank = [0] * N
room_costs = [0] * N  # Para almacenar costes por habitación
total_cost = 0
edges_used = 0

# Procesar aristas ordenadas
for weight, src, dst in candidates:
    if union(parent, rank, src, dst):
        total_cost += weight
        room_costs[src] += weight
        room_costs[dst] += weight
        edges_used += 1
        if edges_used == N - 1:
            break

# Mostrar resultados
print(f"Coste total: {total_cost}")
for i in range(N):
    print(f"H{i}: {room_costs[i]}")

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. sort_candidates: Ordena aristas por coste para procesamiento óptimo
# 2. find/union: Implementación eficiente del Union-Find
# 3. room_costs: Registra acumulación de costes por habitación durante el MST
# =================================================================
# ¿POR QUÉ KRUSKAL?
# 1. El problema requiere un Árbol de Expansión Mínima (MST)
# 2. Necesitamos registrar qué aristas se usan para calcular costes individuales
# 3. Eficiencia demostrada con grafos grandes (M ≤ 200,000)
# =================================================================
# CAMBIOS REALIZADOS:
# 1. Reemplazado update_components por Union-Find eficiente
# 2. Evitado duplicar aristas al construir la lista de candidatos
# 3. Misma salida en formato especificado
# =================================================================
