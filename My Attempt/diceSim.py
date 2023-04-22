# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:44:56 2022

@author: Dineth
"""
from random import randint
from collections import Counter


def dice_sim(*sides):
  number_of_rolls = 1000000 #Number of rolls in simulation
  counts = Counter()
  for roll in range(number_of_rolls):
    counts[sum((randint(1,sides) for side in sides))] += 1
    
    
  print ('\nOUTCOME\tPROBABILITY')
  for outcome in range(len(sides),sum(sides)+1):
    print('{}\t{:0.2f}%'.format(outcome,counts[outcome]*100/number_of_rolls))