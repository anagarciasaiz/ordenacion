n, x = map(int, input().split())
pesos_niños = list(map(int, input().split()))
pesos_niños.sort()
izquierda=0
derecha=n-1

gondolas=0

while izquierda<=derecha:
    if pesos_niños[izquierda]+pesos_niños[derecha]<=x:
        izquierda+=1
        derecha-=1
    else:
        derecha-=1
    gondolas+=1

print(gondolas)
