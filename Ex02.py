# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:51:36 2017

Ex 02
Aluna: Paula Diniz 
TIA: 31760414
"""

n=int(input("Digite um Número: "))
c= 1
soma= 0

if n>0:
    while c<n:
       if n%c==0:
        soma= soma+c
        c= c+ 1
       else:
        c= c+ 1

if soma==n:
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")
