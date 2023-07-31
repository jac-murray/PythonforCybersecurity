#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Jac 7/30/2023

# Import modules

import crypt
import os

# Function to test password

def test_password(algoritm_salt, hashed_password, password_guess):
    # Use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algoritm_salt)
    # Compate salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False  

# Load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top1000.txt", "r")
passwords = f.readlines()

# Prompt user for Algorithm/salt
algorithm_salt = input("What is the algorithm and salt? ")

# Prompt user for salted hash
hashed_password= input("What is the full hashed password? ")

# Loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("Match found: {0}".format(password))
        break