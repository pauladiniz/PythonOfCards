# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:32:15 2017

Ex 01
Aluna: Paula Diniz 
TIA: 31760414
"""

a = 80000
b = 200000
ano = 0

while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1

print ( "A ultrapassa / iguala a B em %d anos" %ano )
