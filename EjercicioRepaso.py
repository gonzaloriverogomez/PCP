# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:38:18 2026

@author: gonza
"""
#Librerias
from scheptk.scheptk import JobShop
from scheptk.util import random_sequence, sorted_value_asc, sorted_index_asc, read_tag
from copy import deepcopy

#Funciones
def positions (lista, objeto):
    return[i for i,x in enumerate(lista) if x==objeto]

def intercambiar (sec, pos1, pos2):
    secint=deepcopy(sec)
    secint[pos1]=sec[pos2]
    secint[pos2]=sec[pos1]
    if (secint[pos1]!=secint[pos2]):
        return secint
    else:
        return print("Es la misma secuencia")
    


#Codigo
inst=JobShop("instanciarepaso.txt")

#S1=inst.random_solution() #Te hace una secuencia extendida para todas las maquinas
S1=[1,0,0,2,3,1,0,2,2,3,1,3]
print(S1)
inst.print_schedule(S1)

obj1=inst.Emax(S1)

print("EL valor de la funcion objetivo 1 es: ",obj1)

earlinessn=inst.Ejn(S1)
print(earlinessn)

jmax=earlinessn.index(obj1)
print(jmax)

for i,x in enumerate (inst.dd):
    print(i,x)
posicionesjmax=positions(S1, jmax)
print (posicionesjmax)

prueba=intercambiar(S1,4,8)
print (prueba)

S2=deepcopy(S1)

for h in range (inst.machines):
    S2=intercambiar(S2,posicionesjmax[h], inst.jobs*inst.machines-1-h)
print (S2)

