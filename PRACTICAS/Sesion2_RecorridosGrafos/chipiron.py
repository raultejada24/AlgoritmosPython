from collections import deque

def bfs_laberinto(matrix, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    q = deque()

    def bfs_aux():
        q.append((0, 0, 1, 0))
        visited[0][0][1 % 2] = True

        while q:
            x, y, turn, dist = q.popleft()

            if matrix[x][y] == 2:
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if turn % 2 == 1:  # Turno impar
                        if not visited[nx][ny][(turn + 1) % 2]:
                            visited[nx][ny][(turn + 1) % 2] = True
                            q.append((nx, ny, turn + 1, dist + 1))
                    else:  # Turno par
                        if matrix[nx][ny] != -1 and not visited[nx][ny][(turn + 1) % 2]:
                            visited[nx][ny][(turn + 1) % 2] = True
                            q.append((nx, ny, turn + 1, dist + 1))
        return -1
    return bfs_aux()


# Lectura de entrada
n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

# Ejecutar BFS y mostrar resultado
print(bfs_laberinto(matrix, n, m))