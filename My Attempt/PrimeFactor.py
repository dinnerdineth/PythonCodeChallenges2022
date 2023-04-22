# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:49:34 2022

@author: Dineth
"""
def prime_number_calc(number):
  factors = list()
  divisor = 2
  while (divisor <= number):
    if number % divisor == 0:
      factors.append(divisor)
      number= number//divisor
    else:
      divisor = divisor + 1
  return factors


if __name__ == '__main__':
  print(prime_number_calc(1321))
  print(prime_number_calc(450))
