
## Greedy - Algoritmo Voraz para el Problema de la Mochila (Knapsack)

def get_best_item(candidates, data):
    """
    Función para seleccionar el ítem con la mejor relación beneficio/peso
    entre los candidatos disponibles teniendo un peso limitado.

    Parámetros:
        - candidates: Conjunto de índices de ítems disponibles.
        - data: Diccionario que contiene los beneficios, pesos y capacidad máxima de la mochila.

    Retorna:
        - El índice del ítem con la mejor relación beneficio/peso.
    """
    best_ratio = -1  # Inicializamos la mejor relación con un valor inválido
    best_item = 0  # Inicializamos el índice del mejor ítem con 0

    # Recorremos todos los candidatos
    for c in candidates:
        ratio = data["profit"][c] / data["weight"][c]  # Calculamos la relación beneficio/peso
        if ratio > best_ratio:  # Si la relación es mejor que la mejor actual
            best_ratio = ratio  # Actualizamos la mejor relación
            best_item = c  # Actualizamos el mejor ítem

    return best_item


def greedy_knapsack(data):
    """
    Algoritmo voraz para resolver el problema de la mochila (Knapsack).

    Partes del Algoritmo Voraz:
        1. Conjunto de Candidatos:
            El conjunto de candidatos son los índices de los ítems disponibles.

        2. Función de Selección:
            En cada paso, se selecciona el ítem con la mejor relación beneficio/peso
            entre los candidatos disponibles.

        3. Función de Factibilidad:
            Una solución es factible si el ítem seleccionado puede ser añadido a la
            mochila sin exceder su capacidad.

        4. Función Objetivo:
            El objetivo es maximizar el beneficio total de los ítems en la mochila.

        5. Función Solución:
            La solución es un vector que indica la fracción de cada ítem que se incluye en la mochila.

    Cuándo usar este algoritmo:
        Este algoritmo es útil cuando se tiene un conjunto de ítems con beneficios y pesos asociados,
        y una capacidad máxima de la mochila. El objetivo es seleccionar los ítems (o fracciones de ellos)
        que maximicen el beneficio total sin exceder la capacidad de la mochila.
    """
    candidates = set()  # Conjunto de candidatos (índices de ítems)
    n = len(data["profit"])  # Número de ítems
    for i in range(n):
        candidates.add(i)  # Añadimos al set todos los ítems como candidatos

    sol = [0] * n  # Vector solución inicializado con 0 (indica que no se ha seleccionado el ítem)
    weight = 0  # Peso actual de la mochila

    # Mientras haya candidatos y no se exceda la capacidad de la mochila
    while candidates and weight < data["W"]:
        best = get_best_item(candidates, data)  # Seleccionamos el mejor ítem
        candidates.remove(best)  # Eliminamos el ítem seleccionado de los candidatos

        # Si el ítem cabe completamente en la mochila
        if weight + data["weight"][best] <= data["W"]:
            sol[best] = 1.0  # Añadimos el ítem completo a la solución
            weight += data["weight"][best]  # Actualizamos el peso de la mochila
        else:
            # Si no cabe completamente, añadimos una fracción del ítem
            sol[best] = (data["W"] - weight) / data["weight"][best]
            weight = data["W"]  # La mochila alcanza su capacidad máxima

    return sol

## Diccionario
data = {
    "profit": [20, 30, 66, 40, 60],  # Beneficios de los ítems
    "weight": [10, 20, 30, 40, 50],  # Pesos de los ítems
    "W": 100  # Capacidad máxima de la mochila
}


sol = greedy_knapsack(data)
print(sol)