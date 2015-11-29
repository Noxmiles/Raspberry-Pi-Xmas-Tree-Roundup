#!/usr/bin/env python
#Endless Christmas Tree Light by Alexander Ochs - noxmiles.de
#based on code by Andrew Gale - pocketmoneytronics.co.uk
import tree
import random
import sys

# Some constants to identify each LED
L0 = 1
L1 = 2
L2 = 4
L3 = 8
L4 = 16
L5 = 32
L6 = 64
ALL = 1+2+4+8+16+32+64 # = 127
NO_LEDS = 0

# All pattern here
def pattern1(): # ascending
  tree.leds_on_and_wait(L0, 0.5)
  tree.leds_on_and_wait(L1, 0.5)
  tree.leds_on_and_wait(L2, 0.5)
  tree.leds_on_and_wait(L3, 0.5)
  tree.leds_on_and_wait(L4, 0.5)
  tree.leds_on_and_wait(L5, 0.5)
  tree.leds_on_and_wait(L6, 0.5)

def pattern2(): # 2 or 3
  tree.leds_on_and_wait(L1+L4, 0.5)
  tree.leds_on_and_wait(L5+L3+L0, 0.5)
  tree.leds_on_and_wait(L2+L6, 0.5)
  tree.leds_on_and_wait(L5+L3+L0, 0.5)

def pattern3(): # blinking
  tree.leds_on_and_wait(ALL, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)

def pattern4():  # ascending, yellow always on
  tree.leds_on_and_wait(L0, 0.5)
  tree.leds_on_and_wait(L0+L1, 0.5)
  tree.leds_on_and_wait(L0+L2, 0.5)
  tree.leds_on_and_wait(L0+L3, 0.5)
  tree.leds_on_and_wait(L0+L4, 0.5)
  tree.leds_on_and_wait(L0+L5, 0.5)
  tree.leds_on_and_wait(L0+L6, 0.5)

def pattern5(): # filling
  tree.leds_on_and_wait(L0, 0.5)
  tree.leds_on_and_wait(L6, 0.5)
  tree.leds_on_and_wait(L5, 0.5)
  tree.leds_on_and_wait(L4, 0.5)
  tree.leds_on_and_wait(L2, 0.5)
  tree.leds_on_and_wait(L1, 0.5)
  tree.leds_on_and_wait(L1+L0, 0.5)
  tree.leds_on_and_wait(L1+L6, 0.5)
  tree.leds_on_and_wait(L1+L5, 0.5)
  tree.leds_on_and_wait(L1+L4, 0.5)
  tree.leds_on_and_wait(L1+L2, 0.5)
  tree.leds_on_and_wait(L1+L3, 0.5)
  tree.leds_on_and_wait(L1+L3+L0, 0.5)
  tree.leds_on_and_wait(L1+L3+L6, 0.5)
  tree.leds_on_and_wait(L1+L3+L5, 0.5)
  tree.leds_on_and_wait(L1+L3+L4, 0.5)
  tree.leds_on_and_wait(L1+L3+L2, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L0, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L6, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L5, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L0, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L6, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L5, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L5+L0, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L5+L6, 0.5)
  tree.leds_on_and_wait(L1+L3+L2+L4+L5+L6+L0, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)
  tree.leds_on_and_wait(L1+L2+L3+L4+L5+L6+L0, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)
  tree.leds_on_and_wait(L1+L2+L3+L4+L5+L6+L0, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)
  tree.leds_on_and_wait(L1+L2+L3+L4+L5+L6+L0, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)
                                                                                                                                                               82,1          34%
def pattern6(): # falling
  tree.leds_on_and_wait(L0, 0.5)
  tree.leds_on_and_wait(L0+L6, 0.5)
  tree.leds_on_and_wait(L0+L6+L5, 0.5)
  tree.leds_on_and_wait(L6+L5+L4, 0.5)
  tree.leds_on_and_wait(L5+L4+L2, 0.5)
  tree.leds_on_and_wait(L4+L2+L3+L1, 0.5)
  tree.leds_on_and_wait(L2+L3+L1, 0.5)
  tree.leds_on_and_wait(L3+L1, 0.5)
  tree.leds_on_and_wait(NO_LEDS, 0.5)

def pattern7(): # blinking, yellow always on
  tree.leds_on_and_wait(L0, 0.5)
  tree.leds_on_and_wait(ALL, 0.5)

def pattern8(): # random LED on
  rand_led = random.randint(0, 6)
  tree.leds_on_and_wait(1<<rand_led, 0.5) # == 2**rand_led

def pattern9(): # candle shine like
  random_led = 0
  for y in range(6):
    random_led += 2**y * random.randint(0,1) * random.randint(0,1) # each LED choosen by 25%
  random_time = random.randint(1,3) # time between 0.1 and 0.3s
  tree.leds_on_and_wait(ALL - random_led, float(random_time)/10)
  random_time = random.randint(1,15) #light time between 0.1 and 1.5s
  tree.leds_on_and_wait(ALL, float(random_time)/10)


tree.setup()
print("Christmas Tree Light. To stop press CTRL + C")

while True:
  try:
    random_led = random.randint(1, 9)
#    print random_led # just for information
    if random_led == 1:
      for y in range(4):
        pattern1()
    elif random_led == 2:
      for y in range(4):
        pattern2()
    elif random_led == 3:
      for y in range(10):
        pattern3()
    elif random_led == 4:
      for y in range(4):
        pattern4()
    elif random_led == 5:
      pattern5()
    elif random_led == 6:
      for y in range(2):
        pattern6()
    elif random_led == 7:
      for y in range(5):
        pattern7()
    elif random_led == 8:
      for y in range(20):
        pattern8()
    elif random_led == 9:
      for y in range(20):
        pattern9()
  except KeyboardInterrupt:
    tree.all_leds_off()
    tree.cleanup()
    sys.exit()

tree.all_leds_off()
tree.cleanup()
