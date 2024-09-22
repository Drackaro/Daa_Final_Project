from itertools import combinations
from collections import Counter

def subset_equality(arr):
    n = len(arr)
    if n == 0:
        return True, [], []
    
    total_sum = sum(arr)
    
    # Si la suma total es impar, no puede haber dos subconjuntos con la misma suma
    if total_sum % 2 != 0:
        return False, None, None
    
    target = total_sum // 2
    
    # Generar todas las combinaciones posibles de subconjuntos de tamaño n/2
    for r in range(1, n // 2 + 1):
        for subset in combinations(arr, r):
            subset_sum = sum(subset)
            
            # Si encontramos un subconjunto cuya suma sea igual al objetivo
            if subset_sum == target:
                subset_count = Counter(subset)
                remaining = []
                
                # Armar el subconjunto restante
                for x in arr:
                    if subset_count[x] > 0:
                        subset_count[x] -= 1
                    else:
                        remaining.append(x)
                
                return True, subset, remaining
    
    return False, None, None