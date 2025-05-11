# =================================================================
# ALGORITMO DE BÚSQUEDA BINARIA PARA "HILO ROJO"
# Objetivo: Para cada pareja de IDs conectados por el hilo rojo,
#           determinar su posición en su correspondiente grupo
# Complejidad: O((N + M) + P·(log N + log M))
#    – Construcción de grupos: O(N + M)
#    – Cada consulta binaria: O(log N) y O(log M)
# =================================================================

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

# =================================================================
# LECTURA DE ENTRADA
# =================================================================
import sys
input = sys.stdin.readline

N = int(input())                          # Nº personas en grupo 1
group1 = list(map(int, input().split()))  # IDs ordenados ascendentemente

M = int(input())                          # Nº personas en grupo 2
group2 = list(map(int, input().split()))  # IDs ordenados ascendentemente

P = int(input())                          # Nº parejas conectadas

# =================================================================
# PROCESAMIENTO DE PAREJAS
# =================================================================
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

# =================================================================
# EXPLICACIÓN CLAVE:
# 1. binary_search():
#    – Iterativa, busca en un array ordenado en O(log n).
#    – Devuelve -1 si no encuentra la clave.
# 2. Entrada ordenada:
#    – No requerimos ordenar, pues los arrays vienen ya ascendentes.
# 3. Complejidad total:
#    – Construcción de listas: O(N + M).
#    – P consultas en O(log N + log M) cada una.
#    – Escalable a N, M ≤ 10^6 y P grande.
# 4. Elección de método:
#    – Búsqueda binaria ideal sobre array ordenado.
#    – Alternativa: Hash map para O(1) por consulta, pero invertiría O(N + M) en memoria.
# =================================================================
