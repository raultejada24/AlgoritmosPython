
def binary_search_exact(v, key):
    """Búsqueda binaria iterativa.
       Devuelve el índice de ‘key’ en ‘v’, o -1 si no existe."""
    low, high = 0, len(v) - 1
    while low <= high:
        mid = (low + high) // 2
        if v[mid] == key:
            return mid       # Encontrado
        elif key < v[mid]:
            high = mid - 1  # Mitad izquierda
        else:
            low = mid + 1   # Mitad derecha
    return -1               # No existe

def lower_bound(v, key):
    """Devuelve la primera posición i en v tal que v[i] ≥ key.
       Si todas las entradas < key, retorna len(v)."""
    low, high = 0, len(v)
    while low < high:
        mid = (low + high) // 2
        if v[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low

N = int(input().strip())                     # Nº de cajas
ids   = []                                   # Lista de IDs (ordenada)
names = {}                                   # Mapa ID → nombre de recompensa
for _ in range(N):
    parts = input().split()
    I = int(parts[0])
    S = ' '.join(parts[1:])  # Corregido: une todas las palabras del nombre
    ids.append(I)
    names[I] = S

# <-- Ordenamos los IDs antes de usar búsquedas binarias y copias -->
# (Según el problema, la entrada ya está ordenada, pero se mantiene por seguridad)
ids.sort()

# Copia de IDs disponibles para ir eliminando
available = ids.copy()

C = int(input().strip())                     # Nº de participantes

for _ in range(C):
    R = int(input().strip())                 # ID elegido por el jugador

    # 0) Si R no existe en el conjunto original, sin recompensa
    if binary_search_exact(ids, R) == -1:
        print("No hay recompensa")
        continue

    # 1) Intentamos hallar caja exacta en disponibles
    idx = binary_search_exact(available, R)
    if idx != -1:
        # Asignamos y eliminamos
        chosen = available.pop(idx)
        print(names[chosen])
        continue

    # 2) No existe exacta → buscamos inserción
    pos = lower_bound(available, R)

    # IDs vecinos
    left_id  = available[pos-1] if pos-1 >= 0         else None
    right_id = available[pos]   if pos   < len(available) else None

    # 3) Determinar el más cercano (desempate a la derecha)
    if left_id is None and right_id is None:
        print("No hay recompensa")
    else:
        if left_id is None:
            chosen = right_id
        elif right_id is None:
            chosen = left_id
        else:
            d_left  = R - left_id
            d_right = right_id - R
            chosen = right_id if d_right <= d_left else left_id

        # Eliminamos y mostramos
        available.remove(chosen)
        print(names[chosen])