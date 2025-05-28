
def get_best_item(candidates, data):
    best_ratio = -1
    best_item = 0
    for c in candidates:
        ratio = data["profit"][c] / data["weight"][c]
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = c
    return best_item

def greedy_knapsack(data):
    candidates = set()
    n = len(data["profit"])
    for i in range(n):
        candidates.add(i)
    sol = [0] * n
    weight = 0

    while candidates and weight < data["W"]:
        best = get_best_item(candidates, data)
        candidates.remove(best)
        if weight + data["weight"][best] <= data["W"]:
            sol[best] = 1.0
            weight += data["weight"][best]
        else:
            sol[best] = (data["W"] - weight) / data["weight"][best]
            weight = data["W"]

    return sol

## Diccionario
data = {
    "profit": [20, 30, 66, 40, 60],  # Beneficios de los ítems
    "weight": [10, 20, 30, 40, 50],  # Pesos de los ítems
    "W": 100  # Capacidad máxima de la mochila
}

sol = greedy_knapsack(data)
print(sol)







































