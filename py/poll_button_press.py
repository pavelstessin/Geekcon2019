#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : poll_button_press.py
Title        :
Project      :
Developers   :  pi
Created      : Fri Sep 20, 2019  09:58pm
Description  :
Notes        :
---------------------------------------------------------------------------
'''
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
while True:
    GPIO.output(27, GPIO.LOW)
    sleep(1)
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    GPIO.output(27, GPIO.HIGH)
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    sleep(1)
# GPIO.add_event_detect(4, GPIO.RISING)
# def my_callback():
    # print 'PUSHED!'

# GPIO.add_event_callback(4, my_callback)
