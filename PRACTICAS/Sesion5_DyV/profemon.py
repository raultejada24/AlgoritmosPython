def binary_search_iterative(arr, start, end, target):
    """
    Busca el índice donde se insertaría target en arr[start:end+1].
    Si target está en arr, devuelve su posición; si no, devuelve
    la posición de inserción (el primer índice > target).
    """
    low, high = start, end
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # Si no lo encontramos, low es la posición de inserción
    return low

# Lectura de datos
n, students = map(int, input().split())
profemon = sorted(map(int, input().split()))

max_count = 0
best_students = []

for _ in range(students):
    stu_id, p1, p2 = map(int, input().split())

    # Índice de inserción / hallazgo para p1 y p2
    p1_idx = binary_search_iterative(profemon, 0, n-1, p1)
    p2_idx = binary_search_iterative(profemon, 0, n-1, p2)

    # Número de profemon en el rango [p1, p2]
    count = p2_idx - p1_idx + 1

    if count > max_count:
        max_count = count
        best_students = [stu_id]
    elif count == max_count:
        best_students.append(stu_id)

# Salida
print(" ".join(map(str, best_students)))
print(max_count)
