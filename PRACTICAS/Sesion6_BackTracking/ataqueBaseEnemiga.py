# =================================================================
# ALGORITMO “YOR BRIAR: ATAQUE A LA BASE ENEMIGA”
# Objetivo: Encontrar el número mínimo de pasos desde la entrada,
#           eliminando todos los enemigos (en cualquier orden),
#           y alcanzando la salida, sin repetir casilla.
# Esquema:
#   1. Identificar puntos clave: entrada (0), cada enemigo (1…E), salida (E+1).
#   2. Para cada par de puntos clave, calcular la distancia mínima en la rejilla
#      mediante BFS (tratando −2 como muro, −1 o 0 como transitables).
#   3. Resolver TSP-Path con DP+bitmask sobre los E enemigos:
#        DP[mask][u] = coste mínimo habiendo visitado el subconjunto 'mask'
#                       de enemigos y acabando en punto clave u (1…E).
#   4. Transición:
#        Para cada v enemigo no en mask:
#          DP[mask ∪ {v}][v] = min( DP[mask][u] + dist[u][v] )
#   5. Respuesta:
#        min_u ( DP[(1<<E)-1][u] + dist[u][E+1] )
# Complejidad:
#   – BFS: O((E+2)·N·M)
#   – DP : O(2^E · E^2)
#   Apto para N,M ≤ 10, E ≤ N·M ≤ 100.
# =================================================================

from collections import deque
import sys

input = sys.stdin.readline

def bfs(start_r, start_c, grid, N, M):
    """BFS desde (start_r,start_c) retorna matriz dist con dist a cada celda."""
    dist = [[-1]*M for _ in range(N)]
    q = deque()
    dist[start_r][start_c] = 0
    q.append((start_r, start_c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != -2 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

# =================================================================
# LECTURA DE ENTRADA Y PUNTOS CLAVE
# =================================================================
N, M, E = map(int, input().split())
ent_r, ent_c = map(int, input().split())
sal_r, sal_c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# Lista de coordenadas de puntos clave: entrada + enemigos + salida
points = [(ent_r, ent_c)]
for r in range(N):
    for c in range(M):
        if grid[r][c] == -1:
            points.append((r, c))
points.append((sal_r, sal_c))

K = len(points)   # = E + 2

# =================================================================
# PRECALCULAR DISTANCIAS ENTRE PUNTOS CLAVE
# =================================================================
# dist_mat[i][j]: distancia mínima de punto i a punto j
dist_mat = [[0]*K for _ in range(K)]
# Para cada punto clave i, BFS sobre toda la rejilla
for i in range(K):
    dr = bfs(points[i][0], points[i][1], grid, N, M)
    for j in range(K):
        dist_mat[i][j] = dr[points[j][0]][points[j][1]]
        # Si es -1, no hay camino → imposible
        if dist_mat[i][j] == -1:
            # Si es entre dos enemigos o entre entrada/salida, no existe solución
            # Marcarlo como “infinito”
            dist_mat[i][j] = 10**9

# =================================================================
# DP + BITMASK PARA TSP-PATH
# =================================================================
FULL = (1 << E) - 1
# DP[mask][u]: mínimo coste visitando 'mask' enemigos, acabando en enemigo índice u (1..E)
dp = [ [10**9]*(E+2) for _ in range(1 << E) ]

# Base: desde entrada (0) a cada enemigo i (punto índice i+1)
for i in range(E):
    dp[1 << i][i+1] = dist_mat[0][i+1]

# Transiciones
for mask in range(1 << E):
    for u in range(1, E+1):
        if not (mask & (1 << (u-1))):
            continue  # u no está en el conjunto 'mask'
        # Intentar ir a un enemigo v no visitado
        for v in range(1, E+1):
            if mask & (1 << (v-1)):
                continue
            new_mask = mask | (1 << (v-1))
            dp[new_mask][v] = min(dp[new_mask][v],
                                  dp[mask][u] + dist_mat[u][v])

# Respuesta: completar ruta hacia salida (punto índice E+1)
ans = 10**9
for u in range(1, E+1):
    ans = min(ans, dp[FULL][u] + dist_mat[u][E+1])

# =================================================================
# SALIDA
# =================================================================
print(ans)
