import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

volumeState = 0

while True:
        buttonState1 = GPIO.input(7)
        buttonState2 = GPIO.input(11)

        if buttonState1 == False and buttonState2 == False and volumeState != 100:
                print("Switch was set to Vol HIGH")
                print(volumeState)
                call(["amixer", "set", "PCM", "unmute"])
                call(["amixer", "set", "PCM", "100%"])
                volumeState = 100
                time.sleep(1)

        if buttonState1 == True and buttonState2 == True and volumeState != 0:
                print("Switch was set to MUTE")
                print(volumeState)
                call(["amixer", "set", "PCM", "mute"])
                volumeState = 0
                time.sleep(1)

        if buttonState1 == True and buttonState2 == False and volumeState != 70:
                print("Switch was set to Vol LOW")
                print(volumeState)
                call(["amixer", "set", "PCM", "unmute"])
                call(["amixer", "set", "PCM", "70%"])
                volumeState = 70
                time.sleep(1)

