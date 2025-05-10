C = int(input())
suma = 0
mejorS = 0
mejorI = 0
segundoS = 0
segundoI = 0
d = {}

for i in range(C):
    d[i] = int(input().split()[1])

    if (d[i] > mejorS):
        segundoS = mejorS
        segundoI = mejorI
        mejorS = d[i]
        mejorI = i


    elif (d[i] > segundoS):
        segundoI = i
        segundoS = d[i]

suma = d[mejorI] + segundoS
print(mejorI, segundoI, suma)