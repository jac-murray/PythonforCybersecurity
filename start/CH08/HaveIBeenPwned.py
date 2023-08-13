#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Jac 8/13

#import modules
import requests
import hashlib

#function to check
def check_haveibeenphoned(sha_prefix):
    pwnd_dict = {}
    #Perform API Request
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)
    
    #confirm if found
    
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwnd_dict[temp_pass[0]] = temp_pass[1]
    return pwnd_dict  
    
#Ask for passwords
new_password = input("What passwords need to be checked? ")

#Hash passwords
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()

#Split hashed_password
sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5:]

pwnd_dict = check_haveibeenphoned(sha_prefix)

if sha_postfix in pwnd_dict.keys():
	print("Password has been compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
	print("Password has not been found, it is safe to use!")
    