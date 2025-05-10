# Función que resuelve el problema del ciclo hamiltoniano usando backtracking
def hamiltoniano_va(x, k, n, grafo):
    # Obtiene los nodos adyacentes al último nodo del camino
    c = adyacentes(x[k - 1], grafo)

    while c:  # Mientras haya candidatos en el conjunto de adyacentes
        candidato = c.pop()  # Toma un candidato del conjunto
        if prometedor(x, candidato, k - 1):  # Verifica si es prometedor
            x[k] = candidato  # Añade el candidato al camino
            if k == n - 1:  # Si se ha completado el camino
                if grafo[candidato][x[0]] == 1:  # Verifica si es un ciclo hamiltoniano
                    print("Ciclo hamiltoniano encontrado:", x)
            else:
                hamiltoniano_va(x, k + 1, n, grafo)  # Llama recursivamente para el siguiente nodo

# Función que obtiene los nodos adyacentes de un nodo dado
def adyacentes(nodo, grafo):
    return {i for i in range(len(grafo)) if grafo[nodo][i] == 1}

# Función que verifica si un candidato es prometedor
def prometedor(x, elem, lim):
    return elem not in x[:lim + 1]  # Es prometedor si no ha sido visitado

# Inicialización de datos y ejecución del algoritmo
n = 5  # Número de nodos
grafo = [  # Matriz de adyacencia del grafo
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
x = [-1] * n  # Inicializa el camino con -1
x[0] = 0  # Comienza desde el nodo 0
hamiltoniano_va(x, 1, n, grafo)  # Llama al procedimiento