#!/usr/bin/env python

import evdev 

def controller_input(port):
    device = evdev.InputDevice(port)#"/dev/input/event0")
    for event in device.read_loop():
        if event.type == 3: #check to see if event type is an absolute axis event can also use evdev.ecodes.EV_ABS instead of 3
            if event.code == 3: 
                return [event.value, 'right']
            elif event.code == 0:
                return [event.value, 'left']
        
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

def main():
    while(True):
        output = controller_input("/dev/input/event0")
        print(output)

main()


#from evdev import InputDevice, categorize, ecodes
#
#device = InputDevice("/dev/input/event0") 
#for event in device.read_loop():
#    #print(event.type)
#    if event.type == ecodes.EV_ABS:
#        print(categorize(event))
#    elif event.type == ecodes.BTN:
#        print(categorize(event))


