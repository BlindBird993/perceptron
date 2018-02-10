# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:37:26 2017

@author: Igor Molchanov
"""

"Perceptron"
from random import choice 
import numpy as np

unit_step = lambda x: 0 if x < 1 else 1

weights = np.random.rand(2)

training_data = [
        (np.array([-10,5]),0), 
        (np.array([-10,18]),0), 
        (np.array([-9,20]),0), 
        (np.array([-5,5]),0), 
        (np.array([-3,0]),0), 
        (np.array([2,-3]),0), 
        (np.array([5,-7]),0), 
        (np.array([5,-8]),0),
        
        (np.array([5,-6]),1), 
        (np.array([5,0]),1), 
        (np.array([4,0]),1), 
        (np.array([1,0]),1), 
        (np.array([1,1]),1), 
        (np.array([-2,5]),1), 
        (np.array([-3,11]),1), 
        (np.array([-6,18]),1),
        (np.array([-10,24]),1)       
        ]
test_data = [
        (np.array([-8,4]),0), 
        (np.array([-6,12]),0), 
        (np.array([-5,6]),0), 
        (np.array([-5,10]),0), 
        (np.array([0,2]),0), 
        (np.array([1,0]),0), 
        (np.array([6,-12]),0), 
        (np.array([6,-14]),0),
        
        (np.array([-7,18]),1), 
        (np.array([-9,30]),1), 
        (np.array([-5,8]),1), 
        (np.array([-1,14]),1), 
        (np.array([1,4]),1), 
        (np.array([2,0]),1), 
        (np.array([2,11]),1), 
        (np.array([3,0]),1),
        (np.array([6,-5]),1)       
        ]
errors = [] 
eta = 0.4 
n = 250

def update_weights(w):
    pass
    
test_set = []
def perceptron(input_arr,w,train):
    w_arr = w
    w1 = w_arr[0]
    w2 = w_arr[1]
    w_sum = input_arr[0][0]*w1 + input_arr[0][1]*w2
    exp_res = input_arr[1]
    actual_res = unit_step(w_sum)
    if (train == True):
        if (actual_res != exp_res):
            err = exp_res-actual_res 
            errors.append(err)
            w1 = w1 + eta*errors[0]*input_arr[0][0]
            w2 = w2 + eta*errors[0]*input_arr[0][1]
    return actual_res

for i in range(n):
    x = choice(training_data)
    perceptron(x,weights,True)



for x in test_data:
    print("{},{}: {} -> {}".format(x[0][0],x[0][1], x[1], perceptron(x,weights,False)))

  
