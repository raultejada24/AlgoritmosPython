## ITERATIVO
def binary_search(v, number):
    low = 0               # Limite inferior
    high = len(v) - 1     # Limite superior

    while low <= high: # Mientras no se crucen pero pueden ser iguales
        mid = (low + high) // 2 # Encuentra el índice medio

        if number == v[mid]: # Justo es el elemento medio
            return mid

        if number < v[mid]: # mitad izquierda
            high = mid - 1
        else:
            low = mid + 1 # mitad derecha

     return -low     # Si no se encuentra, retorna la posición donde debería insertarse como índice negativo


# Lista ordenada
v = [1, 3, 3, 5, 6, 7, 9]
number = 6
index = binary_search(v, number)
if index >= 0: # Si se encuentra el número entonces el index es mayor o igual a 0
    print(index)
else: # Si no se encuentra el número, el índice es negativo
    print("No encontrado, estaria despues de " + str(v[-index - 1]))