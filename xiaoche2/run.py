#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

IN1 = 11
IN2 = 12
IN3 = 16
IN4 = 18


def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(IN1, GPIO.OUT)
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)

def forward():
	GPIO.output(IN1, GPIO.HIGH)
	GPIO.output(IN2, GPIO.LOW)
	GPIO.output(IN3, GPIO.HIGH)
	GPIO.output(IN4, GPIO.LOW)

if __name__ == "__main__":
	init()
	forward()
	time.sleep(3)
	GPIO.cleanup()
