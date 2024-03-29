#!/usr/bin/env python3
"""Control an Arduino over the USB port."""
# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.
# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "COM3"  # Arduino Uno WiFi Rev2
# Imports
import serial
from inputs import get_gamepad
# Functions

# Main
# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

#A_state = 0

while True:
   events = get_gamepad()
   for event in events:
      #print(event.ev_type, event.code, event.state)
      if event.code == "BTN_SOUTH" and event.state == 1:
         #A_state = not A_state
         #print(A_state)
         #usb.write(A_state.to_bytes())
         usb.write((1).to_bytes())


