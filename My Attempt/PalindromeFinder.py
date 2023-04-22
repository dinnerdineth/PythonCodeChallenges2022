# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 17:15:54 2022

@author: Dineth
"""

def palindromeFinder(string):
  string = string.lower()
  string = string.replace(" ","")
  length = len(string)
  palindrome = True
  backwards_string = string[::-1]
  print(string + " " + backwards_string)
  return string == backwards_string

if __name__ == '__main__':
  palindromeFinder("Race car")
  palindromeFinder("Word")