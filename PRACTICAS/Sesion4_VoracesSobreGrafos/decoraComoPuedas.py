from queue import PriorityQueue

def dijkstra(g):
    """
    Implementación de Dijkstra para encontrar las distancias mínimas desde el nodo 0 (sofá).
    - g: Grafo no dirigido representado como lista de adyacencia.
    - Retorna: Lista de distancias mínimas desde el nodo 0 a todos los demás.
    """
    n = len(g)
    dist = [float('inf')] * n  # Inicializar distancias con infinito
    dist[0] = 0  # La distancia al sofá (nodo 0) es 0
    pq = PriorityQueue()
    pq.put((0, 0))  # Cola de prioridad: (distancia, nodo)

    while not pq.empty():
        du, u = pq.get()  # Extraer el nodo con la menor distancia actual
        for v, dv in g[u]:  # Para cada vecino del nodo u
            alt = du + dv  # Distancia alternativa: distancia actual + peso de la arista
            if alt < dist[v]:  # Si encontramos un camino más corto
                dist[v] = alt
                pq.put((alt, v))  # Actualizar la cola de prioridad
    return dist

# --- Lectura de entrada ---
n, m, aleg_time = map(int, input().strip().split())  # Número de habitaciones, puertas y tiempo máximo
g = [[] for _ in range(n)]  # Inicializar grafo como lista de adyacencia

# Construir grafo no dirigido (las puertas son bidireccionales)
for _ in range(m):
    u, v, d = map(int, input().strip().split())
    g[u].append((v, d))
    g[v].append((u, d))  # Añadir arista en ambas direcciones

# --- Calcular tiempo total de decoración ---
dist = dijkstra(g)  # Distancias mínimas desde el sofá (nodo 0)
total_time = sum(dist)  # Suma de todas las distancias mínimas (1 metro = 1 minuto)

# --- Verificar si Aleg puede decorar a tiempo ---
if total_time <= aleg_time:
    print(total_time)  # Tiempo total necesario
else:
    print("Aleg, ¡a decorar!")  # No llega a tiempo