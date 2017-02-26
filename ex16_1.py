#!/usr/bin/env python3.6

from sys import argv

script, filename = argv

print(f"So I am going to print out the file you have just created..")
the_file = open(filename)

print(the_file.read())

the_file.close()
