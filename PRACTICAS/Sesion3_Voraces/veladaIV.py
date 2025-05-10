def greedy_schedule(data):
    """
    Selecciona el máximo número de actividades que no se solapan, utilizando un enfoque voraz.
    Las actividades se ordenan por tiempo de finalización y se seleccionan en orden.
    """
    # Ordenamos las actividades por su tiempo de finalización
    sorted_activities = sorted(zip(data["name"], data["start"], data["finish"]), key=lambda x: x[2])

    selected_activities = []  # Lista para almacenar las actividades seleccionadas
    last_finish_time = -1  # Tiempo de finalización de la última actividad seleccionada

    # Recorremos las actividades ordenadas
    for activity in sorted_activities:
        name, start, finish = activity  # Desempaquetamos la actividad
        # Si la actividad no se solapa con la última seleccionada, la añadimos
        if start >= last_finish_time:
            selected_activities.append(name)
            last_finish_time = finish  # Actualizamos el tiempo de finalización

    return selected_activities  # Retornamos la lista de actividades seleccionadas

# Leemos las entradas
N = int(input().strip())  # Leemos el número de actividades

# Inicializamos un diccionario para almacenar los datos de las actividades
data = {
    "name": [],  # Nombres de las actividades
    "start": [],  # Tiempos de inicio
    "finish": []  # Tiempos de finalización
}

# Leemos los datos de cada actividad
for _ in range(N):
    nombre, I, F = input().strip().split()  # Leemos nombre, inicio y finalización
    data["name"].append(nombre)  # Añadimos el nombre a la lista
    data["start"].append(int(I))  # Añadimos el tiempo de inicio a la lista
    data["finish"].append(int(F))  # Añadimos el tiempo de finalización a la lista

# Obtenemos el horario óptimo utilizando la función greedy_schedule
schedule = greedy_schedule(data)

# Imprimimos el número máximo de actividades que se pueden realizar
print(len(schedule))