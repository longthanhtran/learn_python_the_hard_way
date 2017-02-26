#!/usr/bin/env python3.6

import random

random_array = random.sample(range(0, 10_000), 100)

def find_smallest_position(array):
    """returns position of smallest number from given array"""

    smallest_num = array[0]
    position_of_smallest = 0
    for index, num in enumerate(array[1:], 1):
        if num < smallest_num:
            position_of_smallest = index
    return position_of_smallest

def selection_sort(array):
    """returns sorted array using selection sort algorithm"""

    sorted_array = []
    array_length = len(array)
    while (array):
        sorted_array.append(array.pop(find_smallest_position(array)))
    return sorted_array

print(random_array)
print(selection_sort(random_array))
