# Leer el número de miembros de la familia
N = int(input().strip())
familia = []  # Lista para almacenar la información de cada miembro de la familia

# Leer los datos de cada miembro de la familia
for _ in range(N):
    # Leer el nombre, paciencia, urgencia y tiempo de cada miembro
    nombre, paciencia, urgencia, tiempo = input().strip().split()
    # Añadir a la lista una tupla con: nombre, paciencia, urgencia, ratio (paciencia/urgencia), tiempo
    familia.append((nombre, int(paciencia), int(urgencia), int(paciencia) / int(urgencia), int(tiempo)))

# Ordenar la familia según el ratio (paciencia / urgencia)
familia.sort(key=lambda x: x[3])  # Ordenamos por el ratio de paciencia/urgencia

# Inicializar variables para el orden de uso y el tiempo de espera
orden = []  # Lista para almacenar el orden de uso de la máquina
suma = 0  # Acumulador para el tiempo total de espera
first_name = "zzzzzz"  # Variable para almacenar el nombre alfabéticamente primero
first_time = -1  # Variable para almacenar el tiempo de espera del nombre alfabéticamente primero

# Recorrer la familia ordenada y calcular el tiempo de espera
for f in familia:
    # Añadir el nombre y el tiempo acumulado hasta el momento
    orden.append((f[0], suma))
    # Actualizar el nombre alfabéticamente primero y su tiempo de espera
    if f[0] < first_name:
        first_name = f[0]
        first_time = suma
    # Sumar el tiempo que pasa este miembro en la máquina al acumulador
    suma += f[4]
    # Imprimir el nombre del miembro en el orden de uso
    print(f[0])

# Imprimir el tiempo de espera del nombre alfabéticamente primero
print(first_time)