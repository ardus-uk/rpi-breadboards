#!/usr/bin/python3
# With grateful acknowledgement to 
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3       
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
      
# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.  
# Each of these ports is wired to connect to GND on button press, 
# so set up to detect falling edge detection on each.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
      
# define two threaded callback functions  
# which will run in another thread when events are detected  
def my_callback(channel):  
    print ("\nFalling edge detected on 17") 
  
def my_callback2(channel):  
    print ("\nFalling edge detected on 23")
      
print ("INSTRUCTIONS")
print ("------------\n")
print ("Make sure you have a button connected so that when pressed")
print ("it will connect GPIO port 23 (pin 16) to GND (pin 6)\n")
print ("You will also need a second button connected so that when pressed") 
print ("it will connect GPIO port 17 (pin 11) to GND (pin 14)\n")
print ("Finally, you will need a third button connected so that when pressed")     
print ("it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)\n") 
input("Press Enter when ready\n>")  
      
# when a falling edge is detected on port 17, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  
  
# when a falling edge is detected on port 23, regardless of whatever   
# else is happening in the program, the function my_callback2 will be run  
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)  
    
try:  
    print ("\nWaiting for rising edge on port 24")  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print ("\nRising edge detected on port 24\n\n--- END OF PROGRAM ---\n.")   
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  