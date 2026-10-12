# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:00:35 2026

@author: gonza
"""
#Librerias
from scheptk.scheptk import ParallelMachines
from scheptk.util import random_sequence, sorted_value_asc, sorted_index_asc, read_tag
from copy import deepcopy

inst=ParallelMachines("instancia6.txt")
S1=read_tag("secuencia.txt", "S1")
print (S1)

obj1=inst.SumLj(S1)

#Funciones
def intercambiar (sec, pos1, pos2):
    secint=deepcopy(sec)
    secint[pos1]=sec[pos2]
    secint[pos2]=sec[pos1]
    return secint


#Codigo
S2=intercambiar(S1, 3,7)
print (S2)



