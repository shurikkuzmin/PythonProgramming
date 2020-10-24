# -*- coding: utf-8 -*-
"""
Created on 

"""
age = int(input("Please enter your age: "))

if age < 0:
    print("You are still unborn, man!")
elif age <= 12:
    print("You are such a child!")
elif age <= 19:
    print("You are a monster teenager!")
elif age <= 65:
    print("Eventually you became adult!")
else:
    print("Time to relax!")

