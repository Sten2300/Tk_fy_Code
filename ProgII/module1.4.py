import numpy as np

def count_leaves(nested_list):
    # Basfall: Elementet är ett löv (inte en lista)
    if not isinstance(nested_list, list):
        return 1
    
    # Rekursivt steg: Iterera över elementen och summera
    total = 0
    for item in nested_list:
        total += count_leaves(item)
    return total

print(count_leaves([1, [2, [3, 4], 5], [[6]]]))
