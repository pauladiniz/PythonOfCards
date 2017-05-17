# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:07:18 2017


"""

import math 
divisor = 1
operacao = 0
quantidade = 0
primos = ""

limite = int(input("Digite um Número: "))
if limite > 1: 
    for numero in range(1, limite + 1):
        if numero % 1 == 0:
            divisor += 1
            operacao += 1
            if divisor == 2:
                primos += str (numero) + ""
                quantidade  += 1
                divisor = 1
                print ("Foram necessários",operacao,"comparações para acha os",quantidade)
                for 1 in range (0,len(primos))
print(primos)        
