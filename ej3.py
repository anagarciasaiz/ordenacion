
t = int(input())
for _ in range(t):
    n=int(input())
    horarios=[]
    for _ in range(n):
        a,b=map(int,input().split())
        horarios.append((a,b))

    horarios.sort(key=lambda x:x[1])

    peliculas_vistas=0
    tiempo_ultima_pelicula=0
    for inicio,fin in horarios:
        if inicio>=tiempo_ultima_pelicula:
            peliculas_vistas+=1
            tiempo_ultima_pelicula=fin

    print(peliculas_vistas)

    
