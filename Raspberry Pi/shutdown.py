import RPi.GPIO as GPIO
from time import sleep
from os import system

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
        buttonState = GPIO.input(5)
        if buttonState == True:
                print("Switch was set to off!")
                system("shutdown now -h")
                sleep(1)
