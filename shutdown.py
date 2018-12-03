import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
        buttonState = GPIO.input(5)

        if buttonState == True:
                print("Switch was set to off!")
                os.system("shutdown now -h")
                time.sleep(1)

