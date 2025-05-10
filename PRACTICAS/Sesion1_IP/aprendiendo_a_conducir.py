N = int(input())
d = {
    "Arranca": "Mete primera y pisa acelerador",
    "Cambia de marcha": "Pisa embrague a fondo",
    "Para": "Pisa freno y embrague",
    "Aparca": "Imposible",
    "Rotonda": "POR EL CARRIL DERECHO",
    "Gira": "El intermitente, por favor"
}
for i in range(N):
    entrada = input().strip() #Era por la falta del strip, siempre poner strip
    print(d[entrada])

