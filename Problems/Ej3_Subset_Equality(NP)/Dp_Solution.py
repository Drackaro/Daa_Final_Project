from collections import Counter

def subset_equality_dp(arr):
    total_sum = sum(arr)
    
    # Si la suma total es impar, no puede haber dos subconjuntos con la misma suma
    if total_sum % 2 != 0:
        return False, None, None
    
    target = total_sum // 2
    n = len(arr)
    
    # Tabla de DP, dp[i] será True si podemos formar la suma i
    dp = [False] * (target + 1)
    dp[0] = True  # Siempre es posible formar la suma 0 (con el subconjunto vacío)
    
    # Rastrear el subconjunto que suma 'target'
    prev = [-1] * (target + 1)
    
    for num in arr:
        # Recorrer desde target hacia 0 para evitar reutilizar el mismo número en una iteración
        for i in range(target, num - 1, -1):
            if dp[i]:
                continue
            if dp[i - num]:
                dp[i] = True
                prev[i] = num

        if dp[-1]:
            break

    # Si no podemos formar la suma target, no es posible dividir el conjunto en dos subconjuntos iguales
    if not dp[target]:
        return False, None, None
    
    # Reconstruir el subconjunto que suma 'target'
    subset = []
    while target > 0:
        subset.append(prev[target])
        target -= prev[target]
    
    # El subconjunto restante son los elementos que no están en 'subset'
    subset_count = Counter(subset)
    remaining = []
    for x in arr:
        if subset_count[x] > 0:
            subset_count[x] -= 1
        else:
            remaining.append(x)
    
    return True, subset, remaining