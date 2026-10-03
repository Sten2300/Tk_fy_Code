import random
import math

def count_target(lst, target):
    if len(lst) == 0:
        return 0
    elif lst[0] == target:
        return 1 + count_target(lst[1:], target)
    else:
        return count_target(lst[1:], target)

# print(count_target([1,2,3,43,2,1,1,1,1,1,1,3],1))
    

def sum_digits(tal):
    if tal == 0: 
        return 0
    else:
        return tal % 10 + sum_digits(tal//10) 

print(sum_digits(1111))