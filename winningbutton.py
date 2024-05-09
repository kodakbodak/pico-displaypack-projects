# A simple game for the Pi Pico with the Pimoroni PicoDisplay HAT
# One button is assigned as the "Winning Button"

#############################################################
#############################################################
#############################################################

# Import dependencies
from machine import Pin, Timer

import time

import utime

from pimoroni import Button

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

from pimoroni import RGBLED

import random

# Define the display type, colors type, screen rotation
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0) 

# Create pens of different colors
WHITE = display.create_pen(255, 255, 255)

BLACK = display.create_pen(0, 0, 0)

CYAN = display.create_pen(0, 255, 255)

MAGENTA = display.create_pen(255, 0, 255)

YELLOW = display.create_pen(255, 255, 0)

GREEN = display.create_pen(0, 255, 0)

RED = display.create_pen(255, 0, 0)

# Set the brightness of the backlight (0.0 - 1.0)
display.set_backlight(0.5)

# Set a font to use
display.set_font("bitmap8")

# Define the LED and set its initial color
led = RGBLED(6,7,8)

led1_Pin = Pin(25,Pin.OUT)

led.set_rgb(0, 0, 0)

# Define the buttons
button_a = Button(12)

button_b = Button(13)

button_x = Button(14)

button_y = Button(15)

# A function we can use to clear the screen
def clear():

    display.set_pen(BLACK)

    display.clear()

    display.update()
    
#############################################################
#############################################################
#############################################################
    
# Function for Win Condition
def win():
    
    clear()
    
    display.set_pen(GREEN)
    
    display.text("YOU'RE WINNER!!!", 10, 10, 240, 4)
    
    display.update()
    
    for x in range(5):
        
        led.set_rgb(0, 255, 0)
        
        time.sleep(0.2)
        
        led.set_rgb(0, 0, 0)
        
        time.sleep(0.2)
    
    clear()
    
# Function for Lose Condition
def lose():
    
    clear()
    
    display.set_pen(RED)
    
    display.text("ALL YOUR BASE ARE BELONG TO US", 10, 10, 240, 4)
    
    display.update()
    
    for x in range(2):
        
        led.set_rgb(255, 0, 0)
        
        time.sleep(0.2)
        
        led.set_rgb(0, 0, 0)
        
        time.sleep(0.2)
    
    clear()
        
# Function to pick the winning number
def winning_button():

    random_winner = random.randint(1, 4)
    
    return random_winner
    
# Clear the Screen
clear()

# Set up the pen
display.set_pen(CYAN)
    
# Intro Screen
display.text("Winning Button", 15, 67, 240, 3)

display.update()

time.sleep(2)

clear()

# Main loop for the game
while True:

    winning_number = winning_button()
     
    winner = str(winning_number)
       
    if button_a.read():
         a_pick = 1
         a = str(a_pick)
         
         if a == winner:
             win()
             
         else:
             lose()
           
    elif button_b.read():
         b_pick = 2
         b = str(b_pick)
         
         if b == winner:
             win()
             
         else:
             lose()
             
    elif button_x.read():
         x_pick = 3
         x = str(x_pick)
         
         if x == winner:
             win()
             
         else:
             lose()
     
    elif button_y.read():
         y_pick = 4
         y = str(y_pick)
         
         if y == winner:
             win()
             
         else:
             lose()
    
    else:
             
        display.set_pen(CYAN)

        display.text("Press a button, see if you win!", 10, 10, 240, 4)

        display.update()

        led.set_rgb(0, 0, 0)
        
    # Time between checks for button presses
    time.sleep(0.1)  
        
             
    
             
     





    




















    