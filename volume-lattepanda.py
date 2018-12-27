#!/usr/bin/env python
from time import sleep
from subprocess import call
import signal
import sys

from PyMata.pymata import PyMata #use the PyMata library

# Exit gracefully if run standalone - good for testing
def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Creata a PyMata instance
board = PyMata("/dev/ttyACM0", verbose=TRUE) #Need to verify Arduino port

# Digital pins
switchConnect1 = 0 #Assume D0
switchConnect2 = 1 #Assume D1

# Set the pin modes
board.set_pin_mode(switchConnect1, board.PULLUP, board.DIGITAL) #Pull Up required
board.set_pin_mode(switchConnect2, board.INPUT, board.DIGITAL) #Normal Pull Down
# Maybe add a callback function?

# Set a starting volume state
volumeState = 0

while True:
        switchState1 = board.digital_read(switchConnect1)
        switchState2 = board.digital_read(switchConnect2)

        if switchState1 == False and switchState2 == False and volumeState != 96:
                print("Switch was set to Vol HIGH")
                call(["amixer", "set", "PCM", "unmute"])
                call(["amixer", "set", "PCM", "96%"])
                volumeState = 96
                sleep(1)

        if switchState1 == True and switchState2 == True and volumeState != 0:
                print("Switch was set to MUTE")
                call(["amixer", "set", "PCM", "mute"])
                volumeState = 0
                sleep(1)

        if switchState1 == True and switchState2 == False and volumeState != 75:
                print("Switch was set to Vol LOW")
                call(["amixer", "set", "PCM", "unmute"])
                call(["amixer", "set", "PCM", "75%"])
                volumeState = 75
                sleep(1)
