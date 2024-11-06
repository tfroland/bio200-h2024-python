# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:01:08 2024

@author: tfrol
"""

# Definerer en rekursiv funksjon; en funksjon som kaller på seg selv.
def Fibonacci(n):
    if(n == 0):
        return 0
    
    elif(n == 1):
        return 1
    
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Kaller på funksjonen med tallet 10 for å få det tiende tallet i sekvensen.
print(Fibonacci(10))