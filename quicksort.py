#!/usr/bin/env python3.6

import random

random_array = random.sample(range(0, 10_000), 100)

def quicksort(array):
    """returns sorted array using quicksort algorithm"""
    random.shuffle(array)
    if len(array) < 2:
        return array
    else:
        lower  = []
        higher = []
        pivot  = [array[0]]
        for num in array[1:]:
            if num < pivot[0]:
                lower.append(num)
            elif num > pivot[0]:
                higher.append(num)
            elif num == pivot[0]:
                pivot.append(num)
        return quicksort(lower) + pivot + quicksort(higher)

print(random_array)
print(quicksort(random_array))
