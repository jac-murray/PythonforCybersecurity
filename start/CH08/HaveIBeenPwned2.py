#!/usr/bin/env python3
# Fixed Script that checks passwords agains haveibeenpwned.com API
# https://api.pwnedpasswords.com/range/
# By Jac 8/13

#Import modules
import requests
import hashlib

#Function to check
def check_haveibeenpwned(sha_prefix):
    pwnd_dict = {}
    # Perform API Request
    request_uri = f"https://api.pwnedpasswords.com/range/{sha_prefix}"
    results = requests.get(request_uri)
    
    pwned_list = results.text.splitlines()
    for pwnd_pass in pwned_list:
        hash_suffix, count = pwnd_pass.split(":")
        pwnd_dict[hash_suffix] = count
    return pwnd_dict  

new_password = input("What password needs to be checked? ")

encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest().upper()  # Convert to uppercase

sha_prefix = hashed_password[:5]
sha_postfix = hashed_password[5:]

pwnd_dict = check_haveibeenpwned(sha_prefix)

if sha_postfix in pwnd_dict:
    print(f"Password has been compromised {pwnd_dict[sha_postfix]} times.")
else:
    print("Password has not been found, it is safe to use!")
