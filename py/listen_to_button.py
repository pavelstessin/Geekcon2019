#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : listen_to_button.py
Title        :
Project      :
Developers   :  doron
Created      : Sat Sep 21, 2019  11:39am
Description  :
Notes        :
---------------------------------------------------------------------------
---------------------------------------------------------------------------*/
'''
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.OUT)
GPIO.output(9, GPIO.HIGH)

while True:
    sleep(0.01)
    if GPIO.input(13):
        print("GREEN is PRESSED")
    else:
        print("IDLE")

