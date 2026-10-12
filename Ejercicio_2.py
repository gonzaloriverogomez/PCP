# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:15:20 2026

@author: gonza
"""

from scheptk.scheptk import ParallelMachines
from scheptk.util import random_sequence

instparallel=ParallelMachines("instancia2.txt")

mayorpt=max(instparallel.pt)
print("El mayor PT es", mayorpt)

job_mayorpt=instparallel.pt.index(mayorpt)
print("El trabajo con mayor PT es", job_mayorpt)

S1=random_sequence(instparallel.jobs)
print(S1)
"instparallel.print_schedule(S1)"

instparallel.print_schedule(S1)

pos_job_mayorptS1=S1.index(job_mayorpt)
print("El trabajo con mayor pt en S1 esta en la posicion", pos_job_mayorptS1)

joblastpos=S1[instparallel.jobs-1]
print(instparallel.pt[joblastpos])

compltimes=instparallel.Cjn(S1)
print(compltimes)

