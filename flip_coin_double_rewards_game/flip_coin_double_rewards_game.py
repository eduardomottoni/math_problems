# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:28:59 2023

@author: dudu_

This piece of code give the wrong answer, because it divides the total value per the total of iterations
"""
import numpy as np
import time

def run_game():
    return np.random.choice([True,False])

def game_rule():
    value = 1
    while run_game() == True:
        value *=2
    return value
    
def __main__(n):
    start_time = time.time()  # Record the start time
    total_value = 0
    max_value = 0
    game_value = 0
    for i in range(1, n+1):
        game_value = game_rule()
        total_value += game_value
        if i % 100000 == 0:
            print(f"the partial result for 100000 simulations was {total_value/i} and the maximum value was {max_value}")
        if game_value > max_value:
            max_value = game_value
    total_value_avarege = total_value/n
    print(f"The avarege value for {n} games is {total_value_avarege}, and the maximum value was {max_value}")
    
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds for {n} iterations")
__main__(1000000)