#!/usr/bin/env python3.6

numbers = []

def work_on_list(n, step):
    i = 0
    for i in range(0, n):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")

work_on_list(7, 2)
print("The numbers: ")
for num in numbers:
    print(num, end=' ')
