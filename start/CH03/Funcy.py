#!/usr/bin/env python3
# example workign with Functions
#By Jac 7/21

#function
def send_message():
    good_day = input("Is today a good day? (Y/N) ")

    if good_day in {"Y", "y"}:
        for x in range(10):
            print("Yeah it is!")

send_message()
