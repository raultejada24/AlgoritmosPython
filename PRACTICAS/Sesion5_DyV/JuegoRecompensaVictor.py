def binary_search(v, number, low, high):
    if low > high:
        return -low
    mid = (low + high) // 2 #partimos el array en dos sacando la mitad
    if v[mid] == number: #si el numero buscado esta en el medio justo
        return mid
    elif number < v[mid]:
        return binary_search(v, number, low, mid - 1)
    else: #number > v[mid]. [0,0,0,2,3,4,0] y buscas el 3 y mid = 2, entonces 3 > 2? si, esta a la derecha de mid
        return binary_search(v, number, mid + 1, high)

num_cajas = int(input().strip())
nombre_recompensa = []
identifiers = []
for i in range(num_cajas):
    identificador, nombre_caja = input().strip().split()
    nombre_recompensa.append([nombre_caja])
    identifiers.append(int(identificador))

num_participantes = int(input().strip())
elecciones_participantes = []
for i in range(num_participantes):
    recompensa_elegida = int(input().strip())
    elecciones_participantes.append(recompensa_elegida)

n = len(elecciones_participantes)
elected_identifiers = [False] * len(identifiers)
for i in range(n):
   index = binary_search(identifiers, elecciones_participantes[i], 0, len(identifiers) - 1)

   if index == -1:
       print("No hay recompensa")
   elif elecciones_participantes[i] == identifiers[index] and not elected_identifiers[index]:
       print(nombre_recompensa[index][0])
       elected_identifiers[index] = True
   else:
     if not elected_identifiers[index + 1]:
         print(nombre_recompensa[index + 1][0])
     elif not elected_identifiers[index - 1]:
         print(nombre_recompensa[index - 1][0])
     else: #buscar nuevo elemento libre a la derecha
         while elected_identifiers[index + 1]:
             index += 1
         if not elected_identifiers[index]:
            print(nombre_recompensa[index][0])



