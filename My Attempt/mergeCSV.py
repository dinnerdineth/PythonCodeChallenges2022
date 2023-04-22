# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:58:03 2022

@author: Dineth
"""
import csv

def mergeCSV(input_files,output_path):
  fieldnames = list()
  
  for file in input_files:
    with open(file,'r') as input_csv:
      headings = csv.DictReader(input_csv).fieldnames
      fieldnames.extend(x for x in headings if x not in fieldnames)
      
  with open(output_path,'w',newline = '') as output_csv:
    writer = csv.DictWriter(output_csv, fieldnames)
    writer.writeheader()
    for file in input_files:
      with open(file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        for row in reader:
          writer.writerow(row)
  
  
    