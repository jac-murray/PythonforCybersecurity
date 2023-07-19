#!/usr/bin/env python3
# Sample script that writes to a file
# By Jac 7/18

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#Open file for writing
f = open(dir_path + "/testfile.txt", "w")

#Write to the file
print("hello world")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")

#Close file
f.close()