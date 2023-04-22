# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:41:20 2022

@author: Dineth
"""
import smtplib


def send_email(address,subject,message):
  sender = 'dineth.dayananda@gmail.com'
  
  try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,address,message)
    print ("Email Sent!")
  except:
    print ("Error: Email not sent")
  
  