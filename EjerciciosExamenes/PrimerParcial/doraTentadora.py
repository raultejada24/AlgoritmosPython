
def greedy_schedule(tentadores, max_deadline):
    sol = [None] * (max_deadline + 1)
    for c in tentadores:
        i = c[0]
        found = False
        while i >= 0 and not found:
            if not sol[i]: ## Si el hueco está relleno o no
                sol[i] = c
                found = True
            i -= 1
    return sol


n = int(input().strip())
tentadores = []
max_deadline = -1

for _ in range(n):
    name, max_chapter, attraction = input().strip().split()
    max_deadline = max(max_deadline, int(max_chapter))
    tentadores.append((int(max_chapter), int(attraction), name))

tentadores.sort(reverse= True)
sol = greedy_schedule(tentadores, max_deadline)

for i in range(max_deadline + 1):
    if not sol:
        print("DIA "+str(i)+": SIN TENTADOR")
    else:
        print("DIA "+str(i)+": "+str(sol[i][2])+", LE SOBRAN "+ str(sol[i][0] - i)+" DIAS")