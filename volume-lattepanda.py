#!/usr/bin/env python
from time import sleep
from subprocess import call

# ensure PySerial is installed
# Ubuntu: sudo apt install python-serial
import serial

try:
   arduino = serial.Serial('/dev/ttyACM0', 9600)
except:
   print "Failed to connect on /dev/ttyACM0"

# Set a starting volume state
volumeState = None
volSwitchState = -1

try:
   while True:
      print arduino.readline()
      volSwitchState = arduino.readline().strip()
        
      if volSwitchState == 'HIGH' and volumeState != 96:
         print("Switch was set to volume HIGH")
         call(["amixer", "set", "PCM", "unmute"])
         call(["amixer", "set", "PCM", "96%"])
         volumeState = 96
         sleep(1)

      if volSwitchState == 'MUTE' and volumeState != 0:
         print("Switch was set to MUTE")
         call(["amixer", "set", "PCM", "mute"])
         volumeState = 0
         sleep(1)

      if volSwitchState == 'MEDIUM' and volumeState != 75:
         print("Switch was set to volume MEDIUM")
         call(["amixer", "set", "PCM", "unmute"])
         call(["amixer", "set", "PCM", "75%"])
         volumeState = 75
         sleep(1)

except:
   print ("Failed to read!")
