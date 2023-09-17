from tkinter import *
import RPi.GPIO as gpio
from gpiozero import LED
gpio.setmode(gpio.BCM)
import time

LED = LED(14)
window = Tk()
window.title("Aryanlearns")
l1=Label(window, text ="Enter the string to blink")
l1.grid(row=1, column=1)
window.geometry("300x200")
 
def dot():
    LED.on()
    time.sleep(1.5)
    LED.off()
    time.sleep(0.5)

def dash():
    LED.on()
    time.sleep(2.5)
    LED.off()
    time.sleep(0.5)

def Blinking(INPUT):
 for input_char in INPUT:
    
    if (input_char == 'a'):
        dot()
        dash()

    elif (input_char == 'b'):
        dash()
        dot()
        dot()
        dot()

    elif (input_char == 'c'):
        dash()
        dot()
        dash()
        dot()

    elif (input_char == 'd'):
        dash()
        dot()
        dot()

    elif (input_char == 'e'):
        dot()

    elif (input_char == 'f'):
        dot()
        dot()
        dash()
        dot()

    elif (input_char == 'g'):
        dash()
        dash()
        dot()

    elif (input_char == 'h'):
        dot()
        dot()
        dot()
        dot()

    elif (input_char == 'i'):
        dot()
        dot()

    elif (input_char == 'j'):
        dot()
        dash()
        dash()
        dash()

    elif (input_char == 'k'):
        dash()
        dot()
        dash()

    elif (input_char == 'l'):
        dot()
        dash()
        dot()
        dot()

    elif (input_char == 'm'):
        dash()
        dash()

    elif (input_char == 'n'):
        dash()
        dot()

    elif (input_char == 'o'):
        dash()
        dash()
        dash()

    elif (input_char == 'p'):
        dot()
        dash()
        dash()
        dot()

    elif (input_char == 'q'):
        dash()
        dash()
        dot()
        dash()

    elif (input_char == 'r'):
        dot()
        dash()
        dot()

    elif (input_char == 's'):
        dot()
        dot()
        dot()

    elif (input_char == 't'):
        dash()

    elif (input_char == 'u'):
        dot()
        dot()
        dash()

    elif (input_char == 'v'):
        dot()
        dot()
        dot()
        dash()

    elif (input_char == 'w'):
        dot()
        dash()
        dash()

    elif (input_char == 'x'):
        dash()
        dot()
        dot()
        dash()

    elif (input_char == 'y'):
        dash()
        dot()
        dash()
        dash()

    elif (input_char == 'z'):
        dash()
        dash()
        dot()
        dot()
	

# preparing for gui

def gui():
	input = textbox.get(1.0, "end-1c")
	if len(input)>12:
		l1.config( "Input can be at max 12 characters")
	Blinking(input)
			
textbox = Text(window, height=3, width=33, bg='white')
textbox.grid(row=1, column=1, padx=16, pady=12)

enterButton = Button(window, text='Enter', command=gui)
enterButton.grid(row=2, column=1, padx=8, pady=7)  # Corrected placement and removed left-align

exitbutton = Button(window, text='Exit', command=exit)  # Use exit to exit the application
exitbutton.grid(row=3, column=1, padx=8, pady=7)

window.mainloop()
   my  final code
