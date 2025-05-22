
def binary_search_iter(v, number, low, high):
    """Búsqueda binaria iterativa.
       Devuelve índice del último elemento ≤ number, o -1 si no existe."""
    low, high = 0, len(v) - 1  # Ignoramos parámetros entrantes
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if v[mid] <= number:
            result = mid      # candidato válido
            low = mid + 1     # buscamos más a la derecha
        else:
            high = mid - 1    # buscamos en mitad izquierda
    return result

N = int(input().strip())                              # Nº enemigos
levels = list(map(int, input().split()))              # Niveles (ordenados)

# Si quisieras comprobar ordenamiento:
# levels = merge_sort(levels)
# levels = quick_sort(levels)

# Precalcular suma acumulada de niveles para puntos en O(1)
prefix_sum = [0] * N
prefix_sum[0] = levels[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + levels[i]

M = int(input().strip())  # Nº casos de prueba

for _ in range(M):
    Q = int(input().strip())  # Nivel del Caballero

    # Usamos la versión iterativa; para recursiva, sustituir por:
    # idx = binary_search_rec(levels, Q, 0, N-1)
    idx = binary_search_iter(levels, Q, 0, N-1)

    if idx == -1:
        # Ningún enemigo con nivel ≤ Q
        print("0 0")
    else:
        total_enemies = idx + 1               # Cantidad de enemigos derrotados
        total_points  = prefix_sum[idx]       # Suma de niveles = puntos
        print(f"{total_enemies} {total_points}")


