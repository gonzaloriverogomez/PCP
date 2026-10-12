# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:06:11 2026

@author: gonza
"""

from scheptk.scheptk import SingleMachine
from scheptk.util import random_sequence, sorted_value_asc, sorted_index_asc
from copy import deepcopy

inst=SingleMachine("instancia5.txt")

S1=random_sequence(inst.jobs)
suma1=0
suma2=0
suma3=0
suma4=0

print("La secuencia 1 es: ", S1)
for j in range (inst.jobs):
    suma1=suma1+inst.Tj(S1)[j]
print ("El valor objetivo de la S1 es: ", suma1)
mejorobj=suma1
mejorsec=S1
if suma1<mejorobj:
    mejorobj=suma1
    mejorsec=S1

"inst.print_schedule(S1)"

S2=[i for i in range (inst.jobs)]

print ("La secuencia S2 es: ",S2)
for j in range (inst.jobs):
    suma2=suma2+inst.Tj(S2)[j]
print ("El valor objetivo de la S2 es: ", suma2)
if suma2<mejorobj:
    mejorobj=suma2
    mejorsec=S2

S3=sorted_index_asc(inst.pt) #Da los indices de los trabajos de menor a mayor pt
print ("La secuencia S3 es: ", S3)
for j in range (inst.jobs):
    suma3=suma3+inst.Tj(S3)[j]
print ("El valor objetivo de la S3 es: ", suma3)
if suma3<mejorobj:
    mejorobj=suma3
    mejorsec=S3

"""algo2=sorted_value_asc(inst.pt)  
print(algo2)"""

S4=sorted_index_asc(inst.dd)
print ("La secuencia S4 es: ", S4)
for j in range (inst.jobs):
    suma4=suma4+inst.Tj(S4)[j]
print ("El valor objetivo de la S4 es: ", suma4)
if suma4<mejorobj:
    mejorobj=suma4
    mejorsec=S4
    
print (mejorobj)
print(mejorsec)


