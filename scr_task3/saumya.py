#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:54:43 2021

@author: ssaumya7
"""

import numpy as np

def get_ground_state(num_qubits):
    gs = np.zeros(num_qubits)
    gs[0] = 1
    return gs


def run_program(initial_state, my_circuit):
    num_qubits = int(round( np.log( np.size(initial_state)  )/np.log(2) ))
    
    X = np.array([
            [0, 1],
            [1, 0]
            ])

    H = np.array([
            [1/np.sqrt(2), 1/np.sqrt(2)],
            [1/np.sqrt(2), -1/np.sqrt(2)]
            ])
    
    P0x0 = np.array([
            [1, 0],
            [0, 0]
            ])

    P1x1 = np.array([
            [0, 0],
            [0, 1]
            ])
    
    
    operator = np.identity( np.power(2, num_qubits) )
    for i, gate in enumerate(my_circuit):
        if gate['gate'] == 'cx':

            if 0 == gate['target'][0]:     # control qubit
                op_0 = P0x0
                op_1 = P1x1

            elif 0 == gate['target'][1]:     # control qubit
                op_0 = np.identity(2)
                op_1 = X
                
            else: 
                op_0 = np.identity(2)
                op_1 = np.identity(2)
        
        
            for j in range(1,num_qubits):
                if j == gate['target'][0]:     # control qubit
                    op_0 = np.kron(op_0, P0x0)
                    op_1 = np.kron(op_1, P1x1)

                elif j == gate['target'][1]:     # control qubit
                    op_0 = np.kron(op_0, np.identity(2) )
                    op_1 = np.kron(op_1, X )
                
                else: 
                    op_0 = np.kron(op_0, np.identity(2) )
                    op_1 = np.kron(op_1, np.identity(2) )
                
            op_gate = op_0 + op_1
        
        if gate['gate'] == 'h':
            if 0 == gate['target'][0]:     # control qubit
                op_0 = H
                
            else: 
                op_0 = np.identity(2)        
        
            for j in range(1,num_qubits):
                if j == gate['target'][0]:     # control qubit
                    op_0 = np.kron(op_0, H)
                else: 
                    op_0 = np.kron(op_0, np.identity(2) )
            op_gate = op_0
        
        operator = np.dot(operator, op_gate)       
    
    return np.dot(operator, initial_state)

def measure_all(state_vector):
    num_qubits = int(round( np.log( np.size(state_vector)  )/np.log(2) ))
    p_dist = np.multiply( state_vector, np.conjugate(state_vector) )
    R=np.random.choice( np.power(2, num_qubits) , 1, p=p_dist )
    return R

def get_counts(state_vector, num_shots):
    num_qubits = int(round( np.log( np.size(state_vector)  )/np.log(2) ))
    p_dist = np.multiply( state_vector, np.conjugate(state_vector) )
    R=np.random.choice( np.power(2, num_qubits) , num_shots, p=p_dist )
    
    counts = []
    
    for i in range( np.size(state_vector) ):
        apps = np.count_nonzero(R == i)
#        b_i = "{0:b}".format(i)
        b_i = bin(i)[2:].zfill(num_qubits)
        counts.append( (b_i, apps) )
    return counts









