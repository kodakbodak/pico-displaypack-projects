# A prize selector for the use of our Ethical Hacking Club at tabling events
# Allows for us to make the tabling events a bit more fun

#############################################################
#############################################################
#############################################################
from machine import Pin, Timer

import time

import utime

from pimoroni import Button

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

from pimoroni import RGBLED

import random

#output to onboard led
led1_Pin =Pin(25,Pin.OUT)   

#define the display type, colors type, screen rotation
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0) 

#create pens of different colors
WHITE = display.create_pen(255, 255, 255)

BLACK = display.create_pen(0, 0, 0)

CYAN = display.create_pen(0, 255, 255)

MAGENTA = display.create_pen(255, 0, 255)

YELLOW = display.create_pen(255, 255, 0)

GREEN = display.create_pen(0, 255, 0)

RED = display.create_pen(255, 0, 0)

#more setup
display.set_backlight(0.5)

#font for us to use
display.set_font("bitmap8")

#define the LED
led = RGBLED(6,7,8)

led1_Pin = Pin(25,Pin.OUT)   #onboard led

led.set_rgb(0, 0, 0)

#define the buttons
button_a = Button(12)

button_b = Button(13)

button_x = Button(14)

button_y = Button(15)

#a function we can use to clear the screen
def clear():

    display.set_pen(BLACK)

    display.clear()

    display.update()
    
#############################################################
#############################################################
#############################################################
    
prizes = ['Extra Candy', 'Pi Pico', 'Extra Sticker', 'Spin Again', 