#!/usr/bin/python

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
output_1 = 2
output_2 = 3

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(output_1, GPIO.OUT) 
GPIO.setup(output_2, GPIO.OUT) 

# Initial state
GPIO.output(output_1, GPIO.HIGH)
GPIO.output(output_2, GPIO.HIGH)


userInputPort = ''
userInputState = ''

ports = {'1': output_1, '2': output_2}
states = {'on': GPIO.LOW, 'off': GPIO.HIGH}

while (True):
    userInputPort = input('Which port? 1 or 2 (or quit): ')
    userInputState = input('What state (ON / OFF)? (or quit): ')

    print('Changing port ', userInputPort, ' to ', userInputState)
    GPIO.output(ports[userInputPort], states[userInputState])



