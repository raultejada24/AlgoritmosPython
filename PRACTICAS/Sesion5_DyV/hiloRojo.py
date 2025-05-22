
def binary_search(v, key):
    """Búsqueda binaria iterativa.
       Devuelve el índice de ‘key’ en ‘v’, o -1 si no se encuentra."""
    low, high = 0, len(v) - 1
    while low <= high:
        mid = (low + high) // 2
        if v[mid] == key:
            return mid       # Encontrado
        elif key < v[mid]:
            high = mid - 1  # Mitad izquierda
        else:
            low = mid + 1   # Mitad derecha
    return -1               # No está en el array

import sys
input = sys.stdin.readline

N = int(input())                          # Nº personas en grupo 1
group1 = list(map(int, input().split()))  # IDs ordenados ascendentemente

M = int(input())                          # Nº personas en grupo 2
group2 = list(map(int, input().split()))  # IDs ordenados ascendentemente

P = int(input())                          # Nº parejas conectadas

for _ in range(P):
    x, y = map(int, input().split())     # IDs de la pareja

    idx1 = binary_search(group1, x)      # Posición en grupo 1
    idx2 = binary_search(group2, y)      # Posición en grupo 2

    if idx1 == -1 or idx2 == -1:
        # Al menos uno no pertenece a su grupo
        print("SIN DESTINO")
    else:
        # Imprimimos índices (0-based)
        print(idx1, idx2)
