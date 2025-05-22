# Movimientos: derecha, abajo, izquierda, arriba
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def place_brawler(board, N, M, r, c, rng):
    """
    Devuelve el conjunto de celdas transitables (0)
    que cubriría un brawler en (r,c) con rango rng,
    sin que los muros (-1) bloqueen el ataque.
    """
    cells = {(r, c)}
    for dr, dc in dirs:
        for d in range(1, rng+1):
            rr, cc = r + dr*d, c + dc*d
            if not (0 <= rr < N and 0 <= cc < M):
                break
            cells.add((rr, cc))
    # Filtramos sólo transitables
    return {(rr, cc) for rr, cc in cells if board[rr][cc] == 0}

def backtrack(row, used, current_count):
    global best, N, M, board, brawlers, covered
    if row == N:
        best = max(best, current_count)
        return

    for i in range(N):
        if i in used:
            continue
        _, rng = brawlers[i]
        for c in range(M):
            if board[row][c] != 0 or covered[row][c]:
                continue
            # Cubrimos celdas sin que el muro bloquee
            cells = place_brawler(board, N, M, row, c, rng)
            new_cover = []
            for rr, cc in cells:
                if not covered[rr][cc]:
                    covered[rr][cc] = True
                    new_cover.append((rr, cc))
            backtrack(row+1, used | {i}, current_count + len(new_cover))
            for rr, cc in new_cover:
                covered[rr][cc] = False

# --- Lectura de entrada ---
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
brawlers = [tuple(input().split()) for _ in range(N)]
brawlers = [(name, int(rng)) for name, rng in brawlers]
# --------------------------

covered = [[False]*M for _ in range(N)]
best = 0

backtrack(0, set(), 0)
print(best)

