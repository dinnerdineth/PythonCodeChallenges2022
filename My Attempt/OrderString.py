# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:28:48 2022

@author: Dineth
"""
def order_string(string):
  split = string.split(' ')
  string_length = len(split)
  sorted_string = sorted(string)
  print (sorted_string)
  
  #Solution below
  #return ' '.join(sorted(input.split(), key = str.casefold))