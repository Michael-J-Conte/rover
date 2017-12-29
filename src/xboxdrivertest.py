#!/usr/bin/env python

import evdev 

device = evdev.InputDevice("/dev/xbox1")#"/dev/input/event0")
for event in device.read_loop():
    if event.type == 3: #check to see if event type is an absolute axis event can also use evdev.ecodes.EV_ABS instead of 3
        if event.code == 3: 
            print([event.value, 'right'])
            
        elif event.code == 0:
            print([event.value, 'left'])







### changes graveyard ###


#from evdev import InputDevice, categorize, ecodes
#
#device = InputDevice("/dev/input/event0") 
#for event in device.read_loop():
#    #print(event.type)
#    if event.type == ecodes.EV_ABS:
#        print(categorize(event))
#    elif event.type == ecodes.BTN:
#        print(categorize(event))


        
       # if event.code == 4 and event.value > 0:
       #     print("-x")
       # elif event.code == 4 and event.value < 0:
       #     print("x")

       # elif event.code == 3 and event.value > 0:
       #     print("-y")
       # elif event.code == 3 and event.value < 0:
       #     print("y")
       # print(evdev.categorize(event))
       # print(repr(event))
       # print(event)
