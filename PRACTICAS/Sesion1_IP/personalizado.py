N = int(input())
liderS = ""
liderE = 0
for i in range(N):
    datos = input().strip().split()
    S = datos[0]
    E = int(datos[1])

    if E > liderE:
        liderS = S
        liderE = E

N = N - 1
if N == 1:
    print("Bienvenido equipo de " + liderS + " compuesto por 1 persona")
else:
    print("Bienvenido equipo de " + liderS + " compuesto por " + str(N) + " personas")


