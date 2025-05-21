# =================================================================
# ALGORITMO DE "REY DE DIAMANTES"
# Objetivo: Eliminar de la rejilla cuadrada (N×N) al jugador cuyo identificador
#           sea el menor >= al número atacado por el Rey de Diamantes.
#           Finalmente, mostrar la rejilla con ‘X’ en posiciones eliminadas.
# Complejidad: O(Q·log(N^2) + N^2) con lista ligada en vector (práctico para N≤1000)
# =================================================================
import sys

def binary_search_lower_bound(v, number):
    """Búsqueda binaria iterativa. Devuelve índice del primer elemento >= number,
       o len(v) si no existe ninguno."""
    low, high = 0, len(v) - 1
    pos = len(v)
    while low <= high:
        mid = (low + high) // 2
        if v[mid] >= number:
            pos = mid
            high = mid - 1
        else:
            low = mid + 1
    return pos

# =================================================================
# LECTURA DE ENTRADA RÁPIDA
# =================================================================
data = sys.stdin.read().split()
it = iter(data)
N = int(next(it))
# Leemos rejilla en lista plana
grid_flat = [next(it) for _ in range(N * N)]
# IDs vivos iniciales (mismos que grid_flat pero como enteros)
alive_ids = list(map(int, grid_flat))
M = len(alive_ids)

# Estructura de lista ligada por índices
after = [i + 1 for i in range(M - 1)] + [None]
before = [None] + [i for i in range(M - 1)]
alive = [True] * M
# Máscara para marcar eliminados
erased = [False] * M

# =================================================================
# PROCESO DE ATAQUES
# =================================================================
for atk in map(int, it):
    # 1) Buscar lower_bound en IDs vivos
    idx = binary_search_lower_bound(alive_ids, atk)
    # 2) Saltar a siguiente índice vivo
    while idx is not None and idx < M and not alive[idx]:
        idx = after[idx]
    # 3) Si no hay objetivo válido, continuar
    if idx is None or idx >= M:
        continue
    # 4) Eliminar jugador
    alive[idx] = False
    erased[idx] = True
    p, n = before[idx], after[idx]
    if p is not None:
        after[p] = n
    if n is not None:
        before[n] = p

# =================================================================
# SALIDA RÁPIDA
# =================================================================
out = []
for i in range(M):
    out.append('X' if erased[i] else grid_flat[i])

# Imprimimos fila por fila
write = sys.stdout.write
for r in range(N):
    row = out[r * N:(r + 1) * N]
    write(' '.join(row))
    write('\n')

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. Lectura por bloques y estructura plana para acelerar I/O.
# 2. binary_search_lower_bound() en O(logM) para encontrar lower_bound.
# 3. next/prev arrays para saltos O(1) y eliminaciones en O(1).
# 4. Complejidad global O(Q·log(N^2) + N^2).

