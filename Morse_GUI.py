from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
from morse_coded_letters import letters

# setup pin
GPIO.setmode(GPIO.BCM)
led = LED(14)


#GUI
win = Tk()
win.title = ("Morse code using RPi and LED")
myFont = tkinter.font.Font(family = "Frutiger", size = 12, weight = "bold")

# get a word
word = str(input("Write a word: "))
word = list(word.upper())

# FUNCTIONS

## transform word to characters
def led_switch(time_sleep):
	GPIO.output(led, GPIO.HIGH)
	time.sleep(time_sleep)
	GPIO.output(led, GPIO.LOW)
	time.sleep(0.5)

## LED Control
def led_toggle():
        if led.is_lit:
                led.off()
                button["text"] = "Turn LED ON"
        else:
                led.on()
                button["text"] = "Turn LED OFF"
                
for letter in word:
	time.sleep(2)
	bin_letter = letters[letter]
	print(bin_letter)
	for codes in bin_letter:
		if codes == "-":
			led_switch(0.5)
		elif codes == ".":
			led_switch(0.2)
		elif codes == "/":
			time.sleep(1)
			
def close():
        RPi.GPIO.cleanup()
        win.destroy()
        
def led_control():
        led_switch()
        led_toggle()
        
# WIDGETS
button = Button(win, text = "Turn LED ON", font = myFont, command = led_control, bg = "red", height = 1, width = 24)
button.grid(row = 0, column = 1)

exit_button = Button(win, text = "Exit", font = myFont, command = close, bg = "black", fg = "white", height = 1, width = 24)
exit_button.grid(row = 12, column = 1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever



