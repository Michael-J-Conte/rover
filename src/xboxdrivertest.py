#!/usr/bin/env python

import evdev 

device = evdev.InputDevice("/dev/input/event0")
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == 4 and event.value > 0:
            print("x")
        elif event.code == 4 and event.value < 0:
            print("-x")

        elif event.code == 3 and event.value > 0:
            print("y")
        elif event.code == 3 and event.value < 0:
            print("-y")

        #print(evdev.categorize(event))
        #print(repr(event))
        #print(event)






#from evdev import InputDevice, categorize, ecodes
#
#device = InputDevice("/dev/input/event0") 
#for event in device.read_loop():
#    #print(event.type)
#    if event.type == ecodes.EV_ABS:
#        print(categorize(event))
#    elif event.type == ecodes.BTN:
#        print(categorize(event))


