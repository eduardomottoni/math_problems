# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:58:47 2023

@author: dudu_

for this sample, we will try to optimize the math problem, to reduce the random iterations
"""

import random
import time

def run_game(total_elements):
    return random.choices([True, False], k=total_elements)
def __main__(n):
    start_time = time.time()  # Record the start time
    elements_list = run_game(n)
    # Your list of True and False
    # Initialize a dictionary to count sequences of True
    true_sequences_count = {}
    # Initialize variables to track the current sequence
    current_sequence_size = 0
    number_of_games = 0
    # Iterate over the list
    for element in elements_list:
        if element:
            # If it's True, increment the current sequence size
            current_sequence_size += 1
        else:
            # If it's False, check if the current sequence is greater than zero
            number_of_games += 1
            if current_sequence_size > 0:
                # Increment the count in the dictionary
                true_sequences_count[current_sequence_size] = true_sequences_count.get(current_sequence_size, 0) + 1
                # Reset the current sequence size
                current_sequence_size = 0
    # Check if the last sequence in the list is True
    if current_sequence_size > 0:
        true_sequences_count[current_sequence_size] = true_sequences_count.get(current_sequence_size, 0) + 1
    # Print results
    total_sum = 0
    total_games = number_of_games
    max_value = 0
    for size, count in true_sequences_count.items():
        print(f'True sequence of size {size} occurs {count} times.')
        total_sum += count * (1 << size)
        max_value = max(max_value, size)
    total_games -= sum(true_sequences_count.values())
    bigest_value = 2**max_value
    total_sum += total_games
    average = total_sum / number_of_games
    print(f"The number of games is {number_of_games}, and the average is {average}. The biggest value is {bigest_value}")
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds for {n} iterations")

__main__(1000000000)
