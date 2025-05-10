def get_best_item(contestants, talento_idx, candidates):
    best_item = None
    best_ratio = -1
    for k in candidates:
        contestant = contestants[k]
        ratio = contestant[talento_idx] / contestant[1]  # talento/espacio
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = k
    return best_item


def greedy_knapsack(contestants, weight, i):
    n = len(contestants)
    candidates = set(range(n))  # Usamos índices en lugar de los objetos directamente
    sol = []
    peso_total = 0
    talento_idx = i + 2  # El talento correspondiente a la habitación actual
    acumulado = 0.0

    while candidates and peso_total < weight:
        best_idx = get_best_item(contestants, talento_idx, candidates)
        best = contestants[best_idx]
        candidates.remove(best_idx)  # Eliminamos el índice, no el objeto

        peso_concursante = best[1]
        talento_concursante = best[talento_idx]

        if peso_concursante + peso_total <= weight:
            # Cabe completamente
            peso_total += peso_concursante
            sol.append(best[0])  # Nombre del concursante
            acumulado += talento_concursante
        else:
            # Solo cabe parcialmente
            fraccion = (weight - peso_total) / peso_concursante
            acumulado += talento_concursante * fraccion
            sol.append(best[0])
            peso_total = weight  # La habitación se llena
            # No break para mantener el formato de salida

    print("HABITACION", i, ":", "{:.2f}".format(round(acumulado, 2)))
    for nombre in sol:
        print(nombre)


# Entrada
N = int(input().strip())
contestants = []
for _ in range(N):
    line = input().strip().split()
    name = line[0]
    espacio = int(line[1])
    talentos = list(map(int, line[2:5]))
    contestants.append([name, espacio] + talentos)

capacities = list(map(int, input().strip().split()))

# Procesamos cada habitación
candidatos_restantes = set(range(N))  # Índices de concursantes disponibles

for i in range(3):
    # Creamos una copia de los concursantes pero solo con los disponibles
    contestants_actual = [contestants[idx] for idx in candidatos_restantes]

    # Llamamos a la función con los concursantes disponibles
    greedy_knapsack(contestants_actual, capacities[i], i)

    # Actualizamos los candidatos restantes eliminando los seleccionados
    # Necesitamos obtener los nombres de los seleccionados en esta habitación
    # Esto es un poco complicado porque greedy_knapsack no devuelve la solución
    # Modificamos greedy_knapsack para que devuelva los nombres seleccionados
    # Otra opción es reestructurar el código, pero mantendré tu formato

    # Solución temporal: volver a calcular (ineficiente pero mantiene tu estructura)
    # En una versión optimizada esto se debería reestructurar
    temp_candidates = set(candidatos_restantes)
    temp_sol = []
    temp_peso = 0
    temp_talento_idx = i + 2
    temp_acumulado = 0

    while temp_candidates and temp_peso < capacities[i]:
        best_idx = get_best_item(contestants, temp_talento_idx, temp_candidates)
        best = contestants[best_idx]
        temp_candidates.remove(best_idx)

        if best[1] + temp_peso <= capacities[i]:
            temp_peso += best[1]
            temp_sol.append(best[0])
        else:
            temp_sol.append(best[0])
            temp_peso = capacities[i]

    # Eliminamos los seleccionados de candidatos_restantes
    nombres_seleccionados = set(temp_sol)
    candidatos_restantes = {idx for idx in candidatos_restantes
                            if contestants[idx][0] not in nombres_seleccionados}