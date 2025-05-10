def pivot(v, left, right):
    """Función de partición para Quicksort"""
    pivote = v[left]  # Selecciona el primer elemento como pivote
    i = left + 1  # Índice que avanza desde la izquierda
    j = right  # Índice que retrocede desde la derecha

    # Posiciona i en el primer elemento >= pivote
    while i < right and v[i] < pivote:
        i += 1

    # Posiciona j en el primer elemento <= pivote
    while j > left and v[j] > pivote:
        j -= 1

    # Particionamiento principal
    while i < j:
        # Intercambia elementos mal ubicados
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1

        # Avanza i mientras los elementos sean menores al pivote
        while v[i] < pivote:
            i += 1

        # Retrocede j mientras los elementos sean mayores al pivote
        while v[j] > pivote and j > left:
            j -= 1

    # Coloca el pivote en su posición final
    v[left], v[j] = v[j], v[left]
    return j  # Retorna la posición final del pivote


def quicksort(v, i, j):
    """Algoritmo Quicksort recursivo"""
    if i > j:
        return v  # Caso base: subarray de tamaño 0 o 1

    # Divide y vencerás
    pivote = pivot(v, i, j)  # Obtiene posición del pivote
    quicksort(v, i, pivote - 1)  # Ordena subarray izquierdo
    quicksort(v, pivote + 1, j)  # Ordena subarray derecho


# Ejemplo de uso
v = [4, 6, 4, 67, 4, 3, 4, 4, 65, 34, 5, 3, 5, 3]
quicksort(v, 0, len(v) - 1)
print(v)  # Output: [3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 34, 65, 67]