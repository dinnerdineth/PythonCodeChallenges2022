# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:52:17 2022

@author: Dineth
"""

from collections import Counter

def uniqueWords(file):
  text = open(file,"rt")
  data = text.read()
  words = data.split()
  
  num_words = len(words)
  print ('Number of words = ' + str(num_words))
  
  unique = set(words)
  num_unique = len(unique)
  print ('Number of unique words = ' + str(num_unique))
  
  unique_count = Counter(words)
  
  most_occur = Counter.most_common(unique_count,5)
  print ('Most common unique words = ' + str(most_occur))