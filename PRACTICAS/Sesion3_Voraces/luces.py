def obtener_mejor_pareja(candidates, cualidades, tiempos):
    best_item = -1
    best_ratio = -1.0

    for c in candidates:
        ratio = cualidades[c] / tiempos[c]
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = c
    return best_item

def seleccionar_parejas(cualidad_principal, parejas, tiempo_maximo):
    """
    Selecciona parejas que maximizan la cualidad deseada dentro del tiempo límite

    Args:
        cualidad_principal: "beauty", "intelligence" o "kindness"
        parejas: Lista de (nombre, belleza, inteligencia, amabilidad, tiempo)
        tiempo_maximo: Tiempo total disponible

    Returns:
        tuple: (beneficio_total, lista_parejas)
    """
    # Determinar índice de cualidad
    if cualidad_principal == "beauty":
        cualidad_idx = 1
    elif cualidad_principal == "intelligence":
        cualidad_idx = 2
    else:  # "kindness"
        cualidad_idx = 3

    # Extraer datos relevantes
    nombres = [p[0] for p in parejas]
    cualidades = [p[cualidad_idx] for p in parejas]
    tiempos = [p[4] for p in parejas]

    # Algoritmo greedy
    n = len(parejas)
    candidates = set()
    for c in range(n):
        candidates.add(c)
    beneficio_total = 0.0
    parejas_seleccionadas = []
    tiempo_usado = 0

    while candidates and tiempo_usado < tiempo_maximo:
        best = obtener_mejor_pareja(candidates, cualidades, tiempos)
        candidates.remove(best)

        if tiempos[best] + tiempo_usado <= tiempo_maximo:
            parejas_seleccionadas.append(nombres[best])
            beneficio_total += cualidades[best]
            tiempo_usado += tiempos[best]
        else:
            item_ratio = (tiempo_maximo - tiempo_usado) / tiempos[best]
            parejas_seleccionadas.append(nombres[best])
            beneficio_total += cualidades[best] * item_ratio
            tiempo_usado = tiempo_maximo

    return beneficio_total, parejas_seleccionadas


# Procesamiento de entrada
N = int(input())
for _ in range(N):
    cualidad = input().strip()
    tiempo_max = int(input())
    T = int(input())

    parejas = []
    for _ in range(T):
        datos = input().strip().split()
        nombre = datos[0]
        belleza = int(datos[1])
        inteligencia = int(datos[2])
        amabilidad = int(datos[3])
        tiempo = int(datos[4])
        parejas.append((nombre, belleza, inteligencia, amabilidad, tiempo))

    # Obtener solución
    beneficio, seleccionadas = seleccionar_parejas(cualidad, parejas, tiempo_max)

    # Imprimir resultados
    print(" ".join(seleccionadas))
    print("{:.2f}".format(beneficio))