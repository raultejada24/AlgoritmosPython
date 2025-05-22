# Algoritmo de backtracking para resolver el laberinto

import copy # Para copias profundas de listas

def init_lab():
    f = 10  # Número de filas
    c = 10  # Número de columnas
    lab = [] # Lista para el laberinto
    for _ in range(f):
        lab.append([0] * c)  # Inicializa el laberinto con ceros (celdas libres)
    # Coordenadas de las paredes (celdas bloqueadas)
    walls = [(0,2),(0,7),
             (1,0),(1,2),(1,5),(1,6),(1,8),
             (2,6),(2,8),
             (3,1),(3,4),(3,5),(3,6),
             (4,2),(4,3),(4,7),
             (5,5),(5,7),
             (6,0),(6,3),(6,4),(6,7),(6,9),
             (7,1),(7,2),(7,8),(7,9),
             (8,0),(8,5),(8,7),(8,8),
             (9,2),(9,4),(9,5)]
    for f,c in walls:
        lab[f][c] = float("Inf")  # Marca las paredes con infinito
    return lab

def init_sol(lab):
    sol = copy.deepcopy(lab)  # Inicializa la solución creando una copia del laberinto
    sol[len(sol)-1][len(sol[0])-1] = float("Inf")  # Marca la celda final (abajo derecha) como infinito
    return sol

def is_sol(lab, f, c): # Verifica si se ha llegado a la solución (celda final)
    return f == len(lab)-1 and c == len(lab[0])-1

def is_better(lab, best): # Compara si la solución actual (el valor en esa celda) es mejor que la mejor solución encontrada
    n = len(lab)-1  # Índice de la última fila
    m = len(lab[0]) - 1  # Índice de la última columna
    return lab[n][m] < best[n][m]

def is_feasible(lab, f, c): # Verifica si una celda es factible (dentro de los límites y no bloqueada)
    return (0 <= f < len(lab) and 0 <= c < len(lab[0])) and lab[f][c] == 0 # Si es == 0 está libre

def print_lab(lab): # Imprime el laberinto o la solución
    for i in range(len(lab)):
        for j in range(len(lab[0])): # Lab[0] porque es una lista de listas (las C son el número de listas dentro de cada lista)
            if lab[i][j] == float("Inf"):  # Representa las paredes con "*"
                print("*", end=" ")
            else:  # Imprime los valores de las celdas si no son paredes
                print(lab[i][j], end=" ")
        print()

def lab_va(lab, best, f, c, k): # Algoritmo de backtracking para encontrar la mejor solución
    if is_sol(lab, f, c):  # Si se llega a la solución
        if is_better(lab, best):  # Verifica si es mejor que la solución actual
            best = copy.deepcopy(lab)  # Actualiza la mejor solución
    else:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]  # Direcciones: derecha, abajo, izquierda, arriba
        for d in dir:
            new_f = f + d[0]  # Nueva fila
            new_c = c + d[1]  # Nueva columna
            if is_feasible(lab, new_f, new_c):  # Si la celda es factible
                lab[new_f][new_c] = k  # Marca la celda con el paso actual
                best = lab_va(lab, best, new_f, new_c, k+1)  # Llama recursivamente
                lab[new_f][new_c] = 0  # Restaura la celda (backtracking)
    return best

# Inicializa el laberinto y la solución
lab = init_lab()
best = init_sol(lab)
ini = (0,0)  # Posición inicial
k = 1  # Paso inicial
lab[ini[0]][ini[1]] = k  # Marca la posición inicial
best = lab_va(lab, best, ini[0], ini[1], k+1)  # Llama al algoritmo de backtracking
print_lab(best)  # Imprime la mejor solución encontrada