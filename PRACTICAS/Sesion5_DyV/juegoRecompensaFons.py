def binary_search(boxes, box_choosen):
    low = 0
    high = len(boxes) - 1
    while low <= high:#Hasta que low no sea mayor que high seguimos en el bucle
        mid = (low + high)//2#Calculamos mid
        if box_choosen == boxes[mid][0]:#Caso de que encontramos la caja
            return mid
        if box_choosen < boxes[mid][0]:#Caso de que esta en la parte baja
            high = mid - 1
        else:#Caso de que esta en la parte alta
            low = mid + 1
    return -1


def find_nearest(boxes, boxes_out, sol):#Encontramos la mas cercana
    left = sol -1
    right = sol +1
    n = len(boxes)

    while left >= 0 or right < n:
        if right < n and (left < 0 or (right - sol <= sol - left)):
            if right not in boxes_out:
                return right
            right += 1
        elif left >= 0:
            if left not in boxes_out:
                return left
            left -= 1
    return -1#No hay mas cajas disponibles


N = int(input()) #Inicializamos todas las cajas
boxes = []

for _ in range(N):
    id, name = input().strip().split()
    boxes.append((int(id),name))


M = int(input()) #Buscamos las cajas que piden los participantes

boxes_out = set()
for _ in range(M):
    box_choosen = int(input())
    sol = binary_search(boxes, box_choosen)
    if sol == -1:
        print("No hay recompensa")
    elif sol not in boxes_out: #Si la solucion es factible imprimimos bien
        print(boxes[sol][1])
        boxes_out.add(sol)
    else: #Si la solucion ya esta cogida
        near_sol = find_nearest(boxes, boxes_out, sol)
        if near_sol != -1:
            print(boxes[near_sol][1])
            boxes_out.add(near_sol)
        else:
            print("No hay recompensa")