t = int(input())
for _ in range(t):
    n = int(input())
    identificadores = list(map(int, input().split()))
    
    # Ordena la lista de identificadores para que los duplicados estén juntos
    identificadores.sort()
    
    # Inicializa el contador de identificadores únicos a 1, ya que el primer identificador siempre es único
    cuenta = 1
    
    # Compara elementos adyacentes y cuenta los identificadores únicos
    for i in range(1, n):
        if identificadores[i] != identificadores[i - 1]:
            cuenta += 1
    
    print(cuenta)

    
