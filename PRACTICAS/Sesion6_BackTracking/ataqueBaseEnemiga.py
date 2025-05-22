# Movimientos: derecha, abajo, izquierda, arriba
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def backtrack(grid, visited, f, c, exit_f, exit_c, enemies_left, steps, best):
    # Si llegamos a la salida con todos los enemigos eliminados
    if f == exit_f and c == exit_c:
        if enemies_left == 0 and steps < best[0]:
            best[0] = steps
        return
    # Poda: si ya superamos la mejor solución
    if steps >= best[0]:
        return
    # Explorar vecinos
    for df, dc in dirs:
        nf, nc = f + df, c + dc
        # Comprobar límites
        if not (0 <= nf < len(grid) and 0 <= nc < len(grid[0])):
            continue
        # No atravieses muros ni celdas ya visitadas
        if grid[nf][nc] == -2 or visited[nf][nc]:
            continue
        # Marcar visita
        visited[nf][nc] = True
        was_enemy = False
        if grid[nf][nc] == -1:
            enemies_left -= 1
            was_enemy = True
        # Recursión
        backtrack(grid, visited, nf, nc, exit_f, exit_c, enemies_left, steps+1, best)
        # Restaurar
        if was_enemy:
            enemies_left += 1
        visited[nf][nc] = False

# Lectura de entrada desde stdin
N, M, E = map(int, input().split())         # dimensiones y número de enemigos
sf, sc = map(int, input().split())          # fila y columna de entrada
ef, ec = map(int, input().split())          # fila y columna de salida

grid = [list(map(int, input().split()))     # matriz de la base
        for _ in range(N)]

# Preparamos el array de visitados y contamos enemigos
visited = [[False]*M for _ in range(N)]
visited[sf][sc] = True
initial_enemies = sum(val == -1 for row in grid for val in row)

# Ejecutamos el backtracking
best = [float('inf')]
backtrack(grid, visited, sf, sc, ef, ec, initial_enemies, 1, best)

# Imprimimos el resultado
print(best[0] if best[0] < float('inf') else -1)
