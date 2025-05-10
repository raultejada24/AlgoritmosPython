## Examen

## Greedy - Algoritmo Voraz para Minimizar el Tiempo de Espera en la Planificación de Tareas

def get_best_task(candidates, tasks):
    """
    Función para seleccionar la tarea con el menor tiempo de ejecución entre los candidatos disponibles.

    Parámetros:
        - candidates: Conjunto de índices de tareas disponibles.
        - tasks: Lista de tiempos de ejecución de las tareas.

    Retorna:
        - El índice de la tarea con el menor tiempo de ejecución.
    """
    best_task = 0  # Inicializamos el índice de la mejor tarea con 0
    best_task_time = 0x3f3f3f3f  # Inicializamos el mejor tiempo con un valor grande (infinito/2)

    # Recorremos todos los candidatos
    for c in candidates:
        if tasks[c] < best_task_time:  # Si el tiempo de la tarea actual es menor que el mejor actual
            best_task_time = tasks[c]  # Actualizamos el mejor tiempo
            best_task = c  # Actualizamos la mejor tarea

    return best_task  # Retornamos la tarea con el menor tiempo de ejecución


def order_tasks(tasks):
    """
    Algoritmo voraz para ordenar tareas y minimizar el tiempo de espera total.

    Partes del Algoritmo Voraz:
        1. Conjunto de Candidatos:
            El conjunto de candidatos son los índices de las tareas disponibles.

        2. Función de Selección:
            En cada paso, se selecciona la tarea con el menor tiempo de ejecución entre los candidatos disponibles.

        3. Función de Factibilidad:
            Una solución es factible si todas las tareas se pueden programar en algún orden.

        4. Función Objetivo:
            El objetivo es minimizar el tiempo de espera total de las tareas.

        5. Función Solución:
            La solución es una lista que indica el orden en que se deben ejecutar las tareas.

    Cuándo usar este algoritmo:
        Este algoritmo es útil cuando se tiene un conjunto de tareas con tiempos de ejecución conocidos
        y se desea minimizar el tiempo de espera total. Es especialmente útil en sistemas de planificación
        de tareas donde el orden de ejecución afecta el rendimiento global.
    """
    candidates = set()  # Conjunto de candidatos (índices de tareas)
    for i in range(len(tasks)):
        candidates.add(i)  # Añadimos todas las tareas como candidatos

    sol = []  # Lista para almacenar el orden de las tareas

    # Mientras haya candidatos
    while candidates:
        best = get_best_task(candidates, tasks)  # Seleccionamos la mejor tarea
        candidates.remove(best)  # Eliminamos la tarea seleccionada de los candidatos
        sol.append(best)  # Añadimos la tarea a la solución

    return sol  # Retornamos el orden de las tareas


def calculate_waiting_time(sol, tasks):
    """
    Función para calcular el tiempo de espera de cada tarea y el tiempo de espera total.
    Optimiza el tiempo de espera en un sistema de cola.

    Parámetros:
        - sol: Lista que indica el orden en que se ejecutan las tareas.
        - tasks: Lista de tiempos de ejecución de las tareas.
    """
    times = []  # Lista para almacenar el tiempo de espera de cada tarea
    suma = 0  # Variable para acumular el tiempo de espera total

    # Recorremos las tareas en el orden de la solución
    for i in range(len(sol)):
        task = sol[i]  # Índice de la tarea actual
        suma += tasks[task]  # Acumulamos el tiempo de ejecución de la tarea actual
        times.append(suma)  # Añadimos el tiempo de espera de la tarea actual a la lista

    # Imprimimos los tiempos de espera de cada tarea y el tiempo de espera total
    print("Tiempos de espera de cada tarea:", times)
    print("Tiempo de espera total:", sum(times))


# Datos de entrada
tasks = [5, 10, 3]  # Tiempos de ejecución de las tareas

# Llamada a la función para ordenar las tareas
sol = order_tasks(tasks)

# Imprimimos el orden de las tareas
print("Orden de las tareas:", sol)

# Calculamos y mostramos los tiempos de espera
calculate_waiting_time(sol, tasks)