#!/usr/bin/env python3.6

from sys import argv

script, first, second, third = argv #unpack one variable into multiple ones

explaination = input("Some thing to explain your first argument: ")

print("The script is called: ", script)
print("Your first varialble is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"And here is the {explaination} for the {first} argument")
