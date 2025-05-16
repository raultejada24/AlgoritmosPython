## ITERATIVO
def binary_search(v, number, low, high):
    """Búsqueda binaria iterativa. Devuelve índice si encuentra el elemento"""
    low = 0  # Reinicia low (parámetro inicial no usado)
    high = len(v) - 1  # Reinicia high (parámetro inicial no usado)
    while low <= high:
        mid = (low + high) // 2  # Punto medio
        if number == v[mid]:
            return mid  # Elemento encontrado
        if number < v[mid]:
            high = mid - 1  # Buscar en mitad izquierda
        else:
            low = mid + 1  # Buscar en mitad derecha


# Ejemplo de uso
v = [1, 3, 3, 5, 6, 7, 9]
number = 6

# Versión recursiva con manejo de posición de inserción
index = binary_search(v, number, 0, len(v) - 1)
if index >= 0:
    print(index)  # Índice si se encuentra
else:
    print("No encontrado, estaría después de ", str(v[-index - 1]))  # Posición sugerida