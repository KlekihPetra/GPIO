#!/usr/bin/python

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
relay = {  'rel_01': 11,
            'rel_02': 12,
            'rel_03': 13,
            'rel_04': 15,
            'rel_05': 16,
            'rel_06': 18,
            'rel_07': 22,
            'rel_08': 7,
            'rel_09': 3,
            'rel_10': 5,
            'rel_11': 24,
            'rel_12': 26,
            'rel_13': 19,
            'rel_14': 21,
            'rel_15': 23,
            'rel_16': 8}

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # PCB pin-numbering scheme (physical pin numbers as on the PCB)

for rel, pin in relay.items():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

for rel, pin in relay.items():
    print('Setting relay ', rel, ' to ON.')
    GPIO.output(pin, GPIO.LOW)
    time.sleep(3)

    print('Setting relay ', rel, ' to OFF.')
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(3)


