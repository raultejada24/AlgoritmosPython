import sys

def binary_search_lower_bound(v, number):
    """
    Búsqueda binaria iterativa.
    Devuelve el índice del primer elemento >= number,
    o len(v) si no existe ninguno.
    """
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
# LECTURA RÁPIDA DE ENTRADA
# =================================================================
data = sys.stdin.read().split()
it = iter(data)

# Dimensiones de la rejilla
N = int(next(it))

# Leemos la rejilla en formato plano (lista de strings)
grid_flat = [next(it) for _ in range(N * N)]

# IDs vivos como enteros, mismos que grid_flat
alive_ids = list(map(int, grid_flat))
M = len(alive_ids)

# =================================================================
# ESTRUCTURA DE LISTA LIGADA POR ÍNDICES
# =================================================================
after  = [i + 1 for i in range(M - 1)] + [None]
before = [None] + [i for i in range(M - 1)]
alive  = [True] * M
erased = [False] * M

# =================================================================
# PROCESO DE ATAQUES (iterativo)
# =================================================================
for atk_str in it:
    atk = int(atk_str)
    # 1) Encontrar posición lower_bound
    idx = binary_search_lower_bound(alive_ids, atk)

    # 2) Saltar a siguiente elemento vivo
    while idx is not None and idx < M and not alive[idx]:
        idx = after[idx]

    # 3) Si no hay objetivo, continuar
    if idx is None or idx >= M:
        continue

    # 4) Marcar eliminación
    alive[idx]  = False
    erased[idx] = True

    # 5) Reajustar enlaces
    p, n = before[idx], after[idx]
    if p is not None:
        after[p] = n
    if n is not None:
        before[n] = p

# =================================================================
# SALIDA DE LA REJILLA CON ‘X’ EN POSICIONES ELIMINADAS
# =================================================================
out = [('X' if erased[i] else grid_flat[i]) for i in range(M)]

write = sys.stdout.write
for r in range(N):
    row = out[r * N:(r + 1) * N]
    write(' '.join(row))
    write('\n')
