#A simple game for the Pi Pico with the Pimoroni PicoDisplay HAT

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
    
#function for a win (green led)
def win():
    
    clear()
    
    display.set_pen(GREEN)
    
    display.text("YOU'RE WINNER!!!", 10, 10, 240, 4)
    
    display.update()
    
    led.set_rgb(0, 255, 0)
    
    time.sleep(3)
    
    clear()
    
#function for a loss (red led)
def lose():
    
    clear()
    
    display.set_pen(RED)
    
    display.text("ALL YOUR BASE ARE BELONG TO US", 10, 10, 240, 4)
    
    display.update()
    
    led.set_rgb(255, 0, 0)
    
    time.sleep(3)
    
    clear()
        
#pick the winning button
def winning_button():

    random_winner = random.randint(1, 4)
    
    return random_winner
    

clear()

#main loop for the game
while True:
    
    #display.set_pen(BLACK)
     
    #display.text("Pick a button, see if you win", 10, 10, 240, 4)
     
    #display.update()
     
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
        
        
        display.set_pen(GREEN)

        display.text("Press a button, see if you win!", 10, 10, 240, 4)

        display.update()

        led.set_rgb(255, 255, 255)
        

    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses
        
             
    
             
     





    




















    