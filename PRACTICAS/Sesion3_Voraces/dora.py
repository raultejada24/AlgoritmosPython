def get_best_item(candidates, habilidades, salarios):
    best_ratio = -1.0
    best_item = -1
    for c in candidates:
        ratio = habilidades[c] / salarios[c]
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = c
    return best_item


def formar_equipo(habilidades, salarios, nombres, presupuesto):
    candidates = set()
    n = len(habilidades)
    for c in range(n):
        candidates.add(c)
    habilidad_total = 0.0
    equipo = []
    salario_actual = 0

    while candidates and salario_actual < presupuesto:
        best = get_best_item(candidates, habilidades, salarios)
        candidates.remove(best)

        if salarios[best] + salario_actual <= presupuesto:
            equipo.append(nombres[best])
            habilidad_total += habilidades[best]
            salario_actual += salarios[best]
        else:
            item_ratio = (presupuesto - salario_actual) / salarios[best]
            equipo.append(nombres[best])
            habilidad_total += habilidades[best] * item_ratio
            salario_actual = presupuesto

    return habilidad_total, equipo


# Lectura de datos
N = int(input().strip())
nombres = []
pentester = []
crayontester = []
penciltester = []
salarios = []

for _ in range(N):
    datos = input().split()
    nombres.append(datos[0])
    pentester.append(int(datos[1]))
    crayontester.append(int(datos[2]))
    penciltester.append(int(datos[3]))
    salarios.append(int(datos[4]))

P = int(input())

for _ in range(P):
    X, M = map(int, input().split())

    # Seleccionar habilidades según perfil
    if X == 0:
        habilidades = pentester
    elif X == 1:
        habilidades = crayontester
    else:
        habilidades = penciltester

    # Formar y mostrar equipo
    habilidad, equipo = formar_equipo(habilidades, salarios, nombres, M)
    print("{:.2f}".format(habilidad))
    print(" ".join(equipo))