# -*- coding: utf-8 -*-
"""
Input - Time, Sound, Message

"""
from datetime import datetime
from playsound import playsound

def set_alarm(alarm_time, sound, message):
  current_time = datetime.now()   
  #print (current_time)
  while current_time == alarm_time:
    playsound(sound)
    print (message)
  