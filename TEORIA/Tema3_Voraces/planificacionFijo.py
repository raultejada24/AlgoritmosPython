## Examen

## Greedy - Algoritmo Voraz para Programación de Tareas con Plazos Límite

def get_best_item(data, candidates):
    """
    Función para seleccionar la tarea con el mayor beneficio entre los candidatos disponibles.

    Parámetros:
        - data: Diccionario que contiene los beneficios y plazos límite de las tareas.
        - candidates: Conjunto de índices de tareas disponibles.

    Retorna:
        - El índice de la tarea con el mayor beneficio.
    """
    best_profit = -1  # Inicializamos el mejor beneficio con un valor inválido
    best_item = -1  # Inicializamos el índice de la mejor tarea con un valor inválido

    # Recorremos todos los candidatos
    for c in candidates:
        profit = data["profit"][c]  # Obtenemos el beneficio de la tarea actual
        if profit > best_profit:  # Si el beneficio es mayor que el mejor actual
            best_profit = profit  # Actualizamos el mejor beneficio
            best_item = c  # Actualizamos la mejor tarea

    return best_item  # Retornamos la tarea con el mayor beneficio


def greedy_schedule(data):
    """
    Algoritmo voraz para programar tareas con plazos límite y maximizar el beneficio.

    Partes del Algoritmo Voraz:
        1. Conjunto de Candidatos:
            El conjunto de candidatos son los índices de las tareas disponibles.

        2. Función de Selección:
            En cada paso, se selecciona la tarea con el mayor beneficio entre los candidatos disponibles.

        3. Función de Factibilidad:
            Una solución es factible si la tarea seleccionada puede ser programada dentro de su plazo límite.

        4. Función Objetivo:
            El objetivo es maximizar el beneficio total de las tareas programadas.

        5. Función Solución:
            La solución es un vector que indica qué tarea se programa en cada intervalo de tiempo.

    Cuándo usar este algoritmo:
        Este algoritmo es útil cuando se tiene un conjunto de tareas con beneficios asociados
        y plazos límite para completarlas. El objetivo es programar las tareas de manera que
        se maximice el beneficio total, respetando los plazos límite de cada tarea.
    """
    n = len(data["profit"])  # Número de tareas
    candidates = set()  # Conjunto de candidatos (índices de tareas)
    for i in range(n):
        candidates.add(i)  # Añadimos todas las tareas como candidatos

    sol = [-1] * n  # Vector solución inicializado con -1 (indica que no hay tarea programada)
    last_data = max(data["dead_line"])  # Último plazo límite entre todas las tareas

    j = 0  # Contador para iterar sobre los intervalos de tiempo
    while candidates and j <= last_data:  # Mientras haya candidatos y no se exceda el último plazo
        best_item = get_best_item(data, candidates)  # Seleccionamos la mejor tarea
        candidates.remove(best_item)  # Eliminamos la tarea seleccionada de los candidatos

        i = data["dead_line"][best_item]  # Plazo límite de la tarea seleccionada
        found = False  # Bandera para indicar si se ha encontrado un intervalo válido

        # Buscamos un intervalo disponible dentro del plazo límite
        while i > 0 and not found:
            if sol[i] == -1:  # Si el intervalo está libre
                sol[i] = best_item  # Programamos la tarea en ese intervalo
                found = True  # Marcamos como encontrado
            i -= 1  # Retrocedemos en el tiempo

        j += 1  # Pasamos al siguiente intervalo

    return sol  # Retornamos la solución


# Datos de entrada
data = {
    "profit": [50, 10, 15, 30],  # Beneficios de las tareas
    "dead_line": [2, 1, 2, 1],  # Plazos límite de las tareas
}

# Llamada a la función para programar las tareas
schedule = greedy_schedule(data)

# Imprimimos el resultado
print(schedule)