# Leer el número de casos de prueba
t = int(input())

# Iterar sobre cada caso de prueba
for _ in range(t):
    # Leer los valores de n y k
    n, k = map(int, input().split())
    # Leer la secuencia de números y transformarla para calcular la diferencia con sus índices
    nums = list(map(int, input().split()))
    # Ajustamos nums para que contenga la diferencia entre el índice y el valor (1-indexed)
    nums = [i - nums[i] + 1 for i in range(n)]
 
    # Crear una tabla DP donde dp[i][j] representa el máximo número de índices i
    # que son iguales a su valor en la subarray hasta i, utilizando j movimientos.
    dp = [[-1] * (n + 1) for _ in range(n)]
    # Inicializamos el caso base
    dp[0][1] = 0  # No se puede tener un índice igual a su valor al inicio con un movimiento.
    dp[0][0] = int(nums[0] == 0)  # Si el primer número es 0, tenemos un índice igual.

    # Llenar la tabla DP
    for i in range(1, n):
        for j in range(n + 1):
            # Maximizamos el número de índices fijos:
            # - dp[i-1][j] + int(nums[i] == j): si nums[i] coincide con j entonces nums[i] es índice fijo
            # - dp[i-1][j-1] si j no es 0 (usando un movimiento en nums[i])
            dp[i][j] = max(dp[i - 1][j] + int(nums[i] == j),
                           dp[i - 1][j - 1] if j != 0 else -1)
 
    # Inicializamos la respuesta como -1 (inviable)
    answer = -1
    # Buscamos la primera columna en la última fila que tenga al menos k índices iguales
    for i in range(n):
        if dp[-1][i] >= k:  # Si el número de índices iguales es al menos k
            answer = i  # Guardamos el resultado
            break

    # Imprimimos la respuesta para el caso de prueba actual
    print(answer)