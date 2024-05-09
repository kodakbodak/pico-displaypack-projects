# Decision Maker for Pi Pico with Pimoroni Pico Dislay Pack

#############################################################
#import dependencies
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

#create pens of different colors (bet I wont use mode of them lol)
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

led.set_rgb(0, 0, 0,)

#define the buttons
button_a = Button(12)

button_b = Button(13)

button_x = Button(14)

button_y = Button(15)
#############################################################

#a function we can use to easily and cleanly clear the screen
def clear():

    display.set_pen(BLACK)

    display.clear()

    display.update()

# Flip a coin
def coinflip():
    
    clear()
    
    display.set_pen(WHITE)
    
    side = random.randint(0,1)
    
    if side == 0:
        
        result = "Heads"
    
    elif side == 1:
        
        result = "Tails"
        
    display.text(result, 80, 50, 240, 4)
    
    display.update()
    
    time.sleep(3)
    
    clear()

# Roll a dice
def dice():
    
    clear()
    
    display.set_pen(WHITE)
    
    side = random.randint(1,6)
    
    result = str(side)
    
    display.text(result, 120, 50, 240, 4)
    
    display.update()
    
    time.sleep(3)
    
    clear()

# Rock, Paper, Scissors
def RPS():
    
    clear()
    
    display.set_pen(WHITE)
    
    list = ["Rock", "Paper", "Scissors"]
    
    choice = random.choice(list)
    
    display.text(choice, 70, 50, 240, 4)
    
    display.update()
    
    time.sleep(3)
    
    clear()

# Random 1-100
def random_number():
    
    clear()
    
    display.set_pen(WHITE)
    
    number = random.randint(1, 100)
    
    result = str(number)
    
    display.text(result, 110, 50, 240, 4)
    
    display.update()
    
    time.sleep(3)
    
    clear() 

# Clear the Screen
clear()

# Set up the pen
display.set_pen(WHITE)
    
#Intro Screen
display.text("Decision Maker V1", 15, 67, 240, 3)

display.update()

time.sleep(2)

clear()

# Main Loop
while True:
    
    if button_a.read():
        coinflip()
    
    elif button_b.read():
        RPS()
        
    elif button_x.read():
        dice()
    
    elif button_y.read():
        random_number()
    
    else:
        
        display.set_pen(WHITE)
        
        #Text For Modules
    
        display.text("Coin Flip", 10, 10, 240, 2)
     
        display.text("Dice Roll", 150, 10, 240, 2)
    
        display.text("RPS", 10, 120, 240, 2)
    
        display.text("1-100", 190, 120, 240, 2)
    
        display.text("Choose a module", 15, 67, 240, 3)
    
        display.update()
        
    time.sleep(0.1)
    
    

    
    
    
    
    






