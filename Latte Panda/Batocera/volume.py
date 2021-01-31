#!/usr/bin/env python
from time import sleep
from subprocess import call

# ensure PySerial is installed
# Ubuntu: sudo apt install python-serial
# or pip install pyserial
import serial

try:
   arduino = serial.Serial('/dev/ttyACM1', 57600)
except:
   print "Failed to connect on /dev/ttyACM1"

# Set a starting volume state
volumeState = None
volSwitchState = -1

try:
   while True:
      #print arduino.readline()
      volSwitchState = arduino.readline().strip()
        
      if volSwitchState == 'HIGH' and volumeState != 97:
         print("Switch was set to volume HIGH")
         call(["amixer", "set", "Master", "97%"])
         volumeState = 97
         sleep(1)

      if volSwitchState == 'MUTE' and volumeState != 0:
         print("Switch was set to MUTE")
         call(["amixer", "set", "Master", "0%"])
         volumeState = 0
         sleep(1)

      if volSwitchState == 'MEDIUM' and volumeState != 70:
         print("Switch was set to volume MEDIUM")
         call(["amixer", "set", "Master", "70%"])
         volumeState = 70
         sleep(1)

except:
   print ("Failed to read!")
