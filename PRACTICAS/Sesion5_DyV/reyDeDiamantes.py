# =================================================================
# ALGORITMO DE "REY DE DIAMANTES"
# Objetivo: Eliminar de la rejilla cuadrada (N×N) al jugador cuyo identificador
#           sea el menor >= al número atacado por el Rey de Diamantes.
#           Finalmente, mostrar la rejilla con ‘X’ en posiciones eliminadas.
# Complejidad: O(Q·(log(N^2) + N^2)) con eliminación en lista (práctico para N≤1000)
# =================================================================

## ITERATIVO
def binary_search_iter(v, number, low, high):
    """Búsqueda binaria iterativa. Devuelve índice si encuentra 'number',
       o -1 si no existe."""
    low, high = 0, len(v) - 1
    while low <= high:
        mid = (low + high) // 2
        if v[mid] == number:
            return mid        # Exacto
        elif number < v[mid]:
            high = mid - 1    # Mitad izquierda
        else:
            low = mid + 1     # Mitad derecha
    return -1                  # No existe

## RECURSIVO (inserción)
def binary_search_rec(v, number, low, high):
    """Búsqueda binaria recursiva. Devuelve índice si existe, o -low como
       posición de inserción para el primer elemento > number."""
    if low > high:
        return -low            # Inserción en 'low'
    mid = (low + high) // 2
    if v[mid] == number:
        return mid            # Exacto
    elif number < v[mid]:
        return binary_search_rec(v, number, low, mid - 1)
    else:
        return binary_search_rec(v, number, mid + 1, high)

# =================================================================
# LECTURA DE ENTRADA
# =================================================================
N = int(input().strip())                   # Tamaño de la rejilla (N×N)
# Leemos rejilla y almacenamos posiciones
grid = []
positions = []  # Lista de identificadores en orden ascendente
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    positions.extend(row)

# Copia dinámica de identificadores aún vivos
alive_ids = positions.copy()

# Marcador de eliminados en rejilla
eliminated = [[False]*N for _ in range(N)]

# Ataques del Rey de Diamantes
attacks = list(map(int, input().split()))

# =================================================================
# PROCESAMIENTO DE CADA ATAQUE
# =================================================================
for atk in attacks:
    # Buscamos índice (exacto o inserción)
    res = binary_search_rec(alive_ids, atk, 0, len(alive_ids)-1)
    idx = res if res >= 0 else -res  # Primer ≥ atk
    # Si idx fuera fuera de rango, no se elimina a nadie
    if idx < len(alive_ids):
        eliminated_id = alive_ids.pop(idx)
        # Marcar en rejilla
        # Buscar en grid (valores únicos):
        for r in range(N):
            for c in range(N):
                if grid[r][c] == eliminated_id:
                    eliminated[r][c] = True
                    break
            else:
                continue
            break

# =================================================================
# SALIDA: Imprimir rejilla resultado
# =================================================================
for r in range(N):
    line = []
    for c in range(N):
        if eliminated[r][c]:
            line.append('X')
        else:
            line.append(str(grid[r][c]))
    print(' '.join(line))

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. binary_search_iter(): búsqueda exacta (no usada aquí).
# 2. binary_search_rec(): devuelve índice o -low para inserción, usado
#    como lower_bound para primer valor ≥ ataque.
# 3. alive_ids.pop(idx): elimina al jugador del conjunto vivo.
# 4. Marcamos en "eliminated" la posición en rejilla para X en salida.
# 5. Complejidad: Q·(O(log(N^2)) + O(N^2) buscar en grid) + impresión O(N^2).
#    Apto para N≤1000 en tiempo práctico.
# =================================================================
