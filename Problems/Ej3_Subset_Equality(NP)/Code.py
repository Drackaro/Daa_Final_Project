from itertools import combinations

def subset_equality(arr):
    n = len(arr)
    if n == 0:
        return True, [], []
    
    total_sum = sum(arr)
    
    # Si la suma total es impar, no puede haber dos subconjuntos con la misma suma
    if total_sum % 2 != 0:
        return False, None, None
    
    target = total_sum // 2
    
    # Generar todas las combinaciones posibles de subconjuntos
    for r in range(1, n):
        for subset in combinations(arr, r):
            if sum(subset) == target:
                remaining = [x for x in arr if x not in subset]
                return True, subset, remaining
    
    return False, None, None