#N, C, A = map(int,input().strip().split())
N, C, A = input().strip().split()
A = int(A)

if (C == "r") and (A == 1):
    print("JUGADOR", N, "ELIMINADO")
else:
    print("JUGADOR", N, "CONTINUAR")
