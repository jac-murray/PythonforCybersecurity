#!/usr/bin/env python3
# example workign with conditionals
#By Jac 7/15

good_day = input("Is today a good day? (Y/N)")
if good_day == "Y" or good_day == "y":

  #added loop 7/16
  
  for x in range (10):
    print("Yes, it is!")
if good_day == "N" or good_day == "n":
  print("I'm sorry.")