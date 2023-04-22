# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:46:42 2022

@author: Dineth
"""
import secrets

def generate_password(num_words):
  with open('diceware.wordlist.asc','r') as file:
    lines = file.readlines()[2:7778]
    word_list = [line.split()[1] for line in lines]
    
  words = [secrets.choice(word_list) for i in range(num_words)]
  
  return ' '.join(words)