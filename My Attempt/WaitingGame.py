import random
import time


def waiting_game():
  #Get random time interval, read "Enter" keypress, read second keypress, calculate time, display result
  timer = random.randrange(1,10,1)
  print("Your target time is " + str(timer) + " seconds")
  input("Press Enter to begin")
  timer_start = time.time()
  #start = False
  # while start == False:
    
  #   if keyboard.read_key() == "enter":
  #     start = True
  #     timer_end = time.time()
  input("Press enter after " + str(timer) + " seconds")
  timer_end = time.time()
  total_time = timer_end - timer_start
  delta = total_time - float(timer)
  print ("Game Ended")
  print ("Your time was " + str(total_time) + " seconds")
  if delta > 0:
    print ("You were " + str(delta) + " seconds slow")
  elif delta < 0:
    delta = delta * -1
    print ("You were " + str(delta) + " seconds fast")
  elif delta == 0:
    print ("Congratulations you won!")