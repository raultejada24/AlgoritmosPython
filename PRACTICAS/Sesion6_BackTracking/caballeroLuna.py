# Entrada desde input()
N, M, E = map(int, input().split())
sala = [list(map(int, input().split())) for _ in range(N)]
X, Y, D = map(int, input().split())

# Contador de enemigos encontrados
enemigos_encontrados = 0

# Matriz para almacenar la máxima distancia restante registrada para cada celda
max_steps = [[-1 for _ in range(M)] for _ in range(N)]

# Movimientos: arriba, abajo, izquierda, derecha
movs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def backtracking(x, y, d):
    global enemigos_encontrados

    if d < 0:
        return
    if not (0 <= x < N and 0 <= y < M):
        return
    if sala[x][y] == -1:
        return
    # Si la distancia actual no es mayor que la máxima registrada, no procesar
    if d <= max_steps[x][y]:
        return

    # Guardar el valor previo para restauración (aunque no se restaura en este enfoque)
    prev_max = max_steps[x][y]
    max_steps[x][y] = d  # Actualizar la máxima distancia

    # Si es la primera vez que se procesa esta celda (prev_max == -1), contar enemigo si existe
    if prev_max == -1 and sala[x][y] == 1:
        enemigos_encontrados += 1

    # Explorar todas las direcciones
    for dx, dy in movs:
        backtracking(x + dx, y + dy, d - 1)

# Llamada inicial desde posición (X, Y) con alcance D
backtracking(X, Y, D)

# Resultado
if enemigos_encontrados == E:
    print("ATACA")
else:
    print("CORRE")
