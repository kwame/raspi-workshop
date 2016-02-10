#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random

#Necesito modificar los strings que solicitan el input del usuario, en vez de "left player" usar "jugador izquierdo"? así se lee bien?
#agregando una linea de comentario

left_name = input('left player name is ')
right_name = input('right player name is ')

names = [left_name, right_name]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
right_button = 15
left_button = 14

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO,PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO,PUD_UP)


GPIO.output(led, 1)
time.sleep(random.uniform(5, 10))
GPIO.output(led, 0)

while True:
    if GPIO.input(left_button) == False:
        print (names [0] + " gano")
        break
    if GPIO.input(right_button) == False:
        print (names [1] + " gano")
        break

GPIO.cleanup()
