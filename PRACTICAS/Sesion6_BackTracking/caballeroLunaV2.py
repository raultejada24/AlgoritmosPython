from collections import deque
import sys

def puede_atacar(n, m, E, sala, X, Y, D):
    # dist[x][y] = distancia mínima en pasos desde (X,Y); -1 = no visitado
    dist = [[-1]*m for _ in range(n)]
    q = deque([(X, Y)])
    dist[X][Y] = 0
    enemigos_alcanzados = 0

    # Movimientos ortogonales
    movimientos = [(-1,0), (0,1), (1,0), (0,-1)]

    while q:
        x, y = q.popleft()

        # Si en esta casilla hay un enemigo, lo contamos
        if sala[x][y] == 1:
            enemigos_alcanzados += 1
            # Si ya alcanzó a todos, devolvemos True
            if enemigos_alcanzados == E:
                return True

        # Expandir vecinos
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            # Comprobaciones: dentro de la sala, no es muro y no visitado
            if (0 <= nx < n and 0 <= ny < m and
                sala[nx][ny] != -1 and
                dist[nx][ny] == -1):
                nd = dist[x][y] + 1
                # Solo avanzamos si no superamos D pasos
                if nd <= D:
                    dist[nx][ny] = nd
                    q.append((nx, ny))

    # Si terminamos y no alcanzamos todos, devolvemos False
    return False

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n, m, E = map(int, (next(it), next(it), next(it)))
    sala = [[int(next(it)) for _ in range(m)] for _ in range(n)]
    X, Y, D = map(int, (next(it), next(it), next(it)))
    # Convertir la posición inicial a base 0
    X -= 1
    Y -= 1

    print("ATACA" if puede_atacar(n, m, E, sala, X, Y, D) else "CORRE")

if __name__ == "__main__":
    main()

