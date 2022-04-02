#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program reads in an input, triples it and then writes the result
to a file. 
"""

import sys 
import os
import numpy as np

import random


def main(s):
       
 
    # Open the config file service_*.txt to obtain the 
    # maximum number of sub-jobs per job
    # config_folder = 'config'
    # service_file = os.path.join(config_folder,'service_'+s+'.txt')
    #
    # service_times = np.loadtxt(service_file)
    #
    # # Maximum number of sub-jobs per job
    # J = service_times.shape[1]
    # print(service_times)
    #
    # # As a demonstration, write to a file called dummy_*.txt
    # # in the output directory
    # out_folder = 'output'
    # out_file = os.path.join(out_folder,'dummy_'+s+'.txt')
    #
    # with open(out_file,'w') as file:
    #     file.writelines('The maximum number of sub-jobs per job is '+str(J)+'\n')

    arr = [0.5, 0.3, 0.2]
    print(generate_NO_sub_job(arr))




# Get Number of Server Base on percentage
def generate_NO_sub_job(prob_array):
    temp_sub_job = []
    for i in range(0, len(prob_array)):
        temp_sub_job.append(i + 1)

    return random.choices(temp_sub_job, prob_array)





if __name__ == "__main__":
   # main(sys.argv[1])
   main("3")