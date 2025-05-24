
def is_sol(distance):
    return distance==0 #sera solucion si la distancia que me queda por recorrer es 0

def is_feasible(lab,f,c):
    return ((0<=f<len(lab) and 0<=c<len(lab[0]) and (lab[f][c]==0 or lab[f][c]==-2))) #si no me salgo del rango del tablero y la posicion es 0 (suelo normal) o -2 (enemigo)



def lab_va(lab,best,f,c,k,new_sol,maxDistance):
    if is_sol(maxDistance):
        best=max(new_sol,best)
    else:
        if maxDistance > 0: #si todavia podemos recorrer mas distancia entonces:

            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            for d in dir:
                #calculamos la nueva posicion en el tablero
                new_f=f+d[0]
                new_c=c+d[1]
                #comprobamos si es factible
                if is_feasible(lab,new_f,new_c):
                    #nos guardamos el valor antiguo para restaurarlo en la vuelta atras
                    oldValue=lab[new_f][new_c]

                    if oldValue==-2: #si hemos encontrado un enemigo en el camino lo eliminamos
                        new_sol+=1

                    lab[new_f][new_c]=k
                    best=lab_va(lab,best,new_f,new_c,k+1,new_sol,maxDistance-1) #sumamos 1 al numero de pasos para llevar la cuenta y restamos uno a la distancia que nos queda por recorrer

                    #ahora hacemos la vuelta atras
                    lab[new_f][new_c] = oldValue
                    if oldValue==-2:
                        new_sol-=1
                    #maxDistance+=1 #no hace falta sumarlo porque en las llamadas recursivas se mantiene el valor anterior

    return best


#dimensiones sala y numero de enemigos
n,m,e=map(int,input().strip().split())

lab=[]
for i in range(n):
    lab.append([0]*m)

for i in range(n):
    fila=list(map(int,input().strip().split()))
    for j in range(m):

        if fila[j]==1: #en mi codigo -2 es un enemigo
            lab[i][j]=-2
        else:
            lab[i][j]=fila[j]


#posicion inicial y distancia max a recorrer
x,y,d=map(int,input().strip().split())
k=1
best=0
lab[x][y]=k
sol=lab_va(lab,best,x,y,k+1,0,d)

if sol==e: #si hemos eliminado a todos los enemigos entonces:
    print("ATACA")
else: #sino
    print("CORRE")