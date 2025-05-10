## Greedy - Cambio Voraz

def cambio_moneda(valor, monedas):
    """
    Algoritmo voraz para el problema de cambio de monedas.
    Encontrando la forma más eficiente de dar cambio con las monedas disponibles.

    Partes del Algoritmo Voraz:
        1. Conjunto de Candidatos:
            El conjunto de candidatos es la lista de monedas disponibles, ordenadas de mayor a menor.
            En este caso, monedas = [1, 2, 5, 10, 20, 50, 100, 200, 500].

        2. Función de Selección:
            En cada paso, se selecciona la moneda más grande posible que no exceda el valor restante.
            Esto se hace con la operación valor // monedas[i].

        3. Función de Factibilidad:
            Una solución es factible si la moneda seleccionada no excede el valor restante.
            Esto se verifica en el bucle while con la condición valor > 0.

        4. Función Objetivo:
            El objetivo es minimizar el número total de monedas utilizadas para dar el cambio.
            Esto se logra seleccionando siempre la moneda más grande posible en cada paso.

        5. Función Solución:
            La solución es un vector cambio que indica cuántas monedas
            de cada tipo se utilizan para dar el cambio.
    """

    # Inicializamos un vector para almacenar el número de monedas de cada tipo
    cambio = [0] * len(monedas)  # [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Empezamos desde la moneda más grande (última posición en la lista)
    i = len(monedas) - 1  # Índice para recorrer las monedas de mayor a menor
                          # Empiezan en 0 por eso el -1

    # Mientras haya monedas por procesar y el valor restante sea mayor que 0
    while i >= 0 and valor > 0:
        # Función de Selección: Elegimos la moneda más grande posible
        cambio[i] = valor // monedas[i]  # 2, División entera: número de monedas de monedas[i]

        # Actualizamos el valor restante después de usar las monedas de la denominación actual
        valor = valor % monedas[i]  # 50, Resto: valor que queda por cubrir

        # Pasamos a la siguiente moneda (de mayor a menor)
        i -= 1

    # Devolvemos el vector con el número de monedas de cada tipo (Función Solución)
    return cambio


# Conjunto de monedas disponibles (ordenadas de menor a mayor)
monedas = [1, 2, 5, 10, 20, 50, 100, 200, 500]

valor = 250 # Valor para el que queremos dar el cambio

cambio = cambio_moneda(valor, monedas)
print(cambio)