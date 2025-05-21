# =================================================================
# ALGORITMO DE "REY DE DIAMANTES"
# Usando DSU con path compression para saltos O(α(n)) amortizados.
# Complejidad: O((N^2 + Q)·α(N^2)) con I/O optimizado.
# =================================================================
import sys, threading, bisect

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    # Leemos rejilla en lista plana
    grid = [next(it) for _ in range(N*N)]
    # Copia entera como ints para bisect
    alive_ids = list(map(int, grid))
    M = len(alive_ids)
    # DSU parent: parent[i]=i si i vivo, o siguiente índice
    parent = list(range(M+1))  # parent[M]=M
    erased = [False]*M

    sys.setrecursionlimit(1000000)
    def find(x):
        # path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # Procesamos ataques
    for atk in map(int, it):
        # lower_bound en alive_ids
        idx = bisect.bisect_left(alive_ids, atk)
        # saltar a siguiente vivo
        idx = find(idx)
        if idx >= M:
            continue
        # eliminar
        erased[idx] = True
        parent[idx] = find(idx+1)

    # Salida
    out = sys.stdout.write
    ptr = 0
    for r in range(N):
        row = []
        for _ in range(N):
            row.append('X' if erased[ptr] else grid[ptr])
            ptr += 1
        out(' '.join(row))
        out('\n')

if __name__ == '__main__':
    threading.Thread(target=main).start()
