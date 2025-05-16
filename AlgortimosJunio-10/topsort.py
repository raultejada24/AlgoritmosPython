## TopSort - Ordenacion Topologica con DFS recursivo
## Se usa para ordenar nodos en un grafo dirigido sin ciclos.

## '' = "" (menos al imprimir)

from collections import deque


def topsort(g):
    n = len(g)
    data = { ## Diccionario
        "graph": g,             ## Grafo original
        "state": dict(),        ## Diccionario para almacenar el estado de cada nodo
        "d": dict(),            ## Diccionario para almacenar el tiempo de descubrimiento de cada nodo (izquierda)
        "f": dict(),            ## Diccionario para almacenar el tiempo de finalización de cada nodo. Cuando he acabado con el, he visitado todos sus hijos (derecha)
        "time": 0,              ## Contador de tiempo para el recorrido DFS. Iteraciones
        "list": deque()         ## Mejor para invertirlo al final (cola doble enlazada)
    }

    # Inicializamos los diccionarios de estado, descubrimiento y finalización
    for k in g.keys():                      ## Recorremos el array de claves del dict
        data["state"][k] = "NOT_VISITED"    ## Podemos hacer 0, 1, 2 o con constantes
        data["d"][k] = 0                    ## Sirve para crear la clave en la tabla
        data["f"][k] = 0                    ## Sirve para crear la clave en la tabla

    # Recorremos todos los nodos del grafo
    for k in g.keys():
        if data["state"][k] == "NOT_VISITED":       ## Si el nodo no ha sido visitado
            top_sort_visit(data, k)                 ## Llamamos a la función recursiva para visitar el nodo

    # Imprimimos la lista con el orden topológico
    print(data["list"])


## Función recursiva para visitar los nodos
def top_sort_visit(data, k):
    data["state"][k] = "VISITED"  # Marcamos el nodo como visitado
    data["time"] += 1  # Incrementamos el contador de tiempo
    data["d"][k] = data["time"]  # Registramos el tiempo de descubrimiento del nodo

    # Recorremos todos los nodos adyacentes al nodo actual
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT_VISITED":  # Si el nodo adyacente no ha sido visitado
            top_sort_visit(data, adj)  # Llamada recursiva para visitar el nodo adyacente

    data["state"][k] = "FINISHED"  # Marcamos el nodo como finalizado después de visitar sus adj
    data["time"] += 1  # Incrementamos el contador de tiempo
    data["f"][k] = data["time"]  # Registramos el tiempo de finalización del nodo
    data["list"].appendleft(k)  # Añadimos el nodo al principio de la lista (orden inverso)


## Datos del Grafo (Diccionario)
g = {
    "calcetines": ["zapatos"],  # "calcetines" depende de "zapatos"
    "pantalon": ["zapatos", "cinturon"],  # "pantalon" depende de "zapatos" y "cinturon"
    "camisa": ["cinturon", "jersey"],  # "camisa" depende de "cinturon" y "jersey"
    "zapatos": [],  # "zapatos" no tiene dependencias
    "cinturon": [],  # "cinturon" no tiene dependencias
    "jersey": []  # "jersey" no tiene dependencias
}

## Llamada a la función de ordenación topológica
topsort(g)