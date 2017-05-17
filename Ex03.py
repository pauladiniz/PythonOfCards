# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:12:16 2017

Ex 03
Aluna: Paula Diniz 
TIA: 31760414
"""

n = (input("Digite um numero"))
a=0
b=1
c=2
d=0
while d < n:
    a=a+1
    b=b+1
    c=c+1
    d=a*b*c
if d==n:
    print("Esse numero é triangular!")
else:
    print("Esse numero nao é triangular!")
