#!/usr/bin/python

# External module imports
import RPi.GPIO as GPIO
import datetime

pulseLength = datetime.timedelta(seconds = 5)

# Pin Definitons (board pin-numbering scheme):
drivewayGatePin = 3

# Pin Setup:
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(drivewayGatePin, GPIO.OUT) 

# Initial state
GPIO.output(drivewayGatePin, GPIO.HIGH)

# Open gate (5s pulse)
timerStart = datetime.datetime.now()

print('Pulse start')
GPIO.output(drivewayGatePin, GPIO.LOW)

while (datetime.datetime.now() < timerStart + pulseLength):
    continue

print('Pulse end')
GPIO.output(drivewayGatePin, GPIO.HIGH)


