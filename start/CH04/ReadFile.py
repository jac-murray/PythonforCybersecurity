#!/usr/bin/env python3
# Sample script that reads from a file
# By Jac 7/20


import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Open file for reading

f = open(dir_path + "/hackme.txt", "r")
print("Here is someone to hack - information")

# Read file and print

info = f.read()
print(info)
print(f)

# Close file
f.close()