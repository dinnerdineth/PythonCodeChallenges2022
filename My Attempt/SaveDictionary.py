# -*- coding: utf-8 -*-
"""
Input is a dictionary, save it to a file

Then import the file 
"""
import json

def save_dictionary(filepath,dictionary):
  dict_to_save = dictionary
  filename = filepath + "saveddict.text"
  file = open(filename,"w")
  file.write(json.dumps(dict_to_save))
  
  
  
def retrieve_dictionary(filepath):
  x = 2
