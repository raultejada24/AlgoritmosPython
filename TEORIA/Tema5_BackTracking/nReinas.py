# Función que resuelve el problema de las N reinas usando backtracking
def n_reinas_va(k, n, sol, col, diag45, diag135):
    # Si se han colocado todas las reinas, imprime la solución
    if k == n:
        print(sol)  # Muestra la solución actual
    else:
        # Itera sobre todas las columnas posibles
        for j in range(n):
            # Verifica si la columna y las diagonales están libres
            if j not in col and (j - k) not in diag45 and (j + k) not in diag135:
                sol[k] = j  # Coloca la reina en la columna j
                # Llama recursivamente para colocar la siguiente reina
                n_reinas_va(k + 1, n, sol, col | {j}, diag45 | {j - k}, diag135 | {j + k})
                # No es necesario hacer backtracking explícito porque `sol` se sobrescribe

# Inicialización de datos y ejecución del algoritmo
n = 8  # Número de reinas (puedes cambiar este valor)
sol = [-1] * n  # Inicializa la solución con -1 (sin reinas colocadas)
n_reinas_va(0, n, sol, set(), set(), set())  # Llama al procedimiento con conjuntos vacíos