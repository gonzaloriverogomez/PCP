# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 08:41:48 2026

@author: gonza
"""

from scheptk.scheptk import FlowShop
from scheptk.util import random_sequence

inst=FlowShop ("instancia3(1).txt")
print ("Los tiempos de proceso son", inst.pt)
print ("El Tp del segundo trabajo en la primera maquina es: ", inst.pt[0][1])
print(inst.pt[0])

sumapt=[]
for j in range (inst.jobs):
    suma=0
    for i in range (inst.machines):
        suma=suma+inst.pt[i][j]
    
    sumapt.append(suma)
    print("Los pt totales del trabajo", j+1, "es ", sumapt[j])

minpt=min(sumapt)
trabajomin=sumapt.index(minpt)
print (trabajomin)

S1=random_sequence(inst.jobs)
print(S1)

inst.print_schedule(S1)
compltimes=inst.Cj(S1)
print (compltimes)

cij,order=inst.ct(S1) #Aprenderse bien como funciona la funcion ct
print (cij)
print(order)

cijn=inst.ctn(S1)
print (cijn)

Sparcial=[S1[0],S1[1]]

Sparcial.insert(1,S1[inst.jobs-2])
print(Sparcial)

cijn=inst.ctn(Sparcial) 
print (cijn)





