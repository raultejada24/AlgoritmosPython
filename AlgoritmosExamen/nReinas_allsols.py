'''
def is_feasible(sol, row, col):
    is_feas = True
    i = 1
    while is_feas and i <= row:
        feas_col = sol[row-i] == -1 or sol[row-i] != col
        feas_diag1 = sol[row-i] == -1 or col-i < 0 or sol[row-i] != col - i
        feas_diag2 = sol[row-i] == -1 or col+1 >= len(sol) or sol[row-i] != col + i
        is_feas = feas_col and feas_diag1 and feas_diag2
        i += 1
    return is_feas
'''

import time

def is_sol(sol, row): # Verifica si la solución es completa
    return row == len(sol)  # Es solución si todas las reinas están colocadas

def is_feasible(sol, row, col): # Verifica si es factible colocar una reina en la posición (row, col)
    for i in range(row):  # Recorre las filas anteriores
         if sol[i] == col or abs(sol[i] - col) == abs(i - row): # Verifica conflictos en la misma columna o en las diagonales
            return False
    return True


def nqueens(sol, n, row):
    if is_sol(sol, row): # " Caso base": Si se ha llegado a una solución completa, se imprime
        print(sol)
    else:
        col = 0  # Comienza desde la primera columna
        # Intenta colocar una reina en cada columna de la fila actual
        while col < n:
            if is_feasible(sol, row, col): # Si es factible colocar la reina en (row, col)
                sol[row] = col  # Coloca la reina
                nqueens(sol, n, row+1)  # Llama recursivamente para la siguiente fila
                sol[row] = -1  # Restaura el estado (backtracking)
            col += 1  # Pasa a la siguiente columna

n = 12 # Número de reinas
sol = [-1] * n
ini = time.time()
nqueens(sol, n, 0)
print("TOTAL TIEMPO EJECUCION: "+str(time.time()-ini))

# ======================================================================================================================

# Codigo para solo una solucion:

# Tanto IS_SOL como IS_FEASIBLE son iguales a los anteriores

def nqueens_onesol(sol, n, found, row): # Variable nueva FOUND
    if is_sol(sol, row):
        found = True
    else:
        col = 0
        while not found and col < n:
            if is_feasible(sol, row, col):
                sol[row] = col
                sol, found = nqueens_onesol(sol, n, found, row+1)
                if not found:
                    sol[row] = -1
            col += 1
    return sol, found

n = 20
sol = [-1] * n
ini = time.time()
sol, found = nqueens_onesol(sol, n, False, 0)
if found:
    print(sol)
else:
    print("No solution found")
print("TOTAL: "+str(time.time()-ini))
