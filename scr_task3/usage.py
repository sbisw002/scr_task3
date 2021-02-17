#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:11:04 2021

@author: ssaumya7
"""

import saumya as sm
import numpy as np

# I only implemented h and cx
my_circuit = [
{ "gate": "h", "target": [0] }, 
{ "gate": "cx", "target": [0, 1] }, 
{ "gate": "cx", "target": [0, 1] }
]


#my_circuit = [
#{ "gate": "cx", "target": [0, 2] }
#]


num_qubits = 3
my_qpu = sm.get_ground_state( np.power(2, num_qubits) )

final_state = sm.run_program(my_qpu, my_circuit)
print('\n final state:')
print(final_state)


M_o = sm.measure_all(final_state)
print('\n Measured outcome:')
print(M_o)

counts = sm.get_counts(final_state, 10)
print('\n counts:')
print(counts)






