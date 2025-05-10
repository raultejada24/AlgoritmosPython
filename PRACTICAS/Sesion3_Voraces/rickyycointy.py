def cambio_monedas(N, monedas):
    monedas.sort(reverse=True) ## monedas_ord = sorted(monedas, reverse=True)
    resultado = {}
    totalmonedas = 0
    for moneda in monedas:
        if N >= moneda:
            cantidad = N // moneda
            resultado[moneda] = cantidad
            totalmonedas += cantidad
            N = N - (cantidad * moneda)

    print(totalmonedas)
    resultado_ord = sorted(resultado.keys(), reverse=True)
    for moneda in resultado_ord:
        print(f"{moneda}: {resultado[moneda]}")


# Lectura de entrada
N = int(input())
monedas = list(map(int, input().strip().split()))

# Llamar a la función
cambio_monedas(N, monedas)