import copy

def add(sol, data, i):
    sol['obj'][i] = 1
    sol['w'] += data['w'][i]
    sol['v'] += data['v'][i]

def remove(sol, data, i):
    sol['obj'][i] = 0
    sol['w'] -= data['w'][i]
    sol['v'] -= data['v'][i]

def best(sol_1, sol_2):
    return copy.deepcopy(sol_1 if sol_1['v'] > sol_2['v'] else sol_2)

def is_feasible(sol, data, i):
    return sol['w'] + data['w'][i] <= data['W']

def knapsack_0_1(data, sol, best_sol, k):
    if k == data['n']:
        best_sol = best(best_sol, sol)
    else:
        if is_feasible(sol, data, k):
            add(sol, data, k)
            best_sol = knapsack_0_1(data, sol, best_sol, k + 1)
            remove(sol, data, k)
        best_sol = knapsack_0_1(data, sol, best_sol, k + 1)
    return best_sol

# === Entrada ===
n, P, B = map(int, input().split())
nombres = []
pesos = []
beneficios = []

for _ in range(n):
    parts = input().split()
    nombres.append(parts[0])
    pesos.append(int(parts[1]))
    beneficios.append(int(parts[2]))

data = {
    'n': n,
    'W': P,
    'w': pesos,
    'v': beneficios
}

def init_sol(data):
    return {'obj': [0] * data['n'], 'w': 0, 'v': 0}

sol = init_sol(data)
best_sol = init_sol(data)
best_sol = knapsack_0_1(data, sol, best_sol, 0)

# === Salida ===
objetos = [nombres[i] for i in range(n) if best_sol['obj'][i]]
objetos.sort()
print(' '.join(objetos))
print(f"{best_sol['w']} {best_sol['v']}")
print("SE VA" if best_sol['v'] > B else "VUELVE")
