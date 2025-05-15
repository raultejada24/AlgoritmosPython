def merge(left, right, v):
    """Fusión de dos subarrays ordenados (left y right) en el array principal v"""
    l = 0  # Índice para left
    r = 0  # Índice para right
    i = 0  # Índice para v

    # Compara elementos de ambos subarrays
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            v[i] = left[l]
            l += 1
        else:
            v[i] = right[r]
            r += 1
        i += 1

    # Copia los elementos restantes del subarray no vacío
    if r == len(right):
        f = l
        resto = left
    else:
        f = r
        resto = right

    for j in range(f, len(resto)):
        v[i] = resto[j]
        i += 1


def merge_sort(v):
    """Algoritmo Merge Sort recursivo"""
    if len(v) == 1:  # Caso base
        return
    else:
        mid = len(v) // 2
        merge_sort(v[:mid]) ## Ordena mitad izquierda: de 0 a mid
        merge_sort(v[mid:]) ## Ordena mitad derecha: de mid a final(n) - 1
        merge(v[:mid], v[mid:], v)  # Fusiona ambas mitades


# Ejemplo de uso
v = [3, 1, 4, 1, 7, 9, 2, 6, 5, 3, 5, 8]
merge_sort(v)
print(v)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9]