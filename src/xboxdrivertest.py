#!/usr/bin/env python
import evdev 

device = evdev.InputDevice("/dev/xbox1")
for event in device.read_loop():
    if event.type == 3: #check to see if event type is an absolute axis event
        if event.code == 4: 
            print([event.value, 'right analog'])
        elif event.code == 16:
            print([event.value, 'D-Pad X'])
        elif event.code == 17:
            print([event.value, 'D-Pad Y'])
        elif event.code == 2:
            print([event.value, 'left trigger'])
        elif event.code == 5:
            print([event.value, 'right trigger'])
        elif event.code == 1:
            print([event.value, 'left analog'])
    
    elif event.type == 1:#check to see if event type is a button event
        if event.code == 307:
            print([event.value, 'X button'])
        elif event.code == 308:
            print([event.value, 'Y button'])
        elif event.code == 310:
            print([event.value, 'left bumper'])
        elif event.code == 311:
            print([event.value, 'right bumper'])
        elif event.code == 304:
            print([event.value, 'A button'])
        elif event.code == 305:
            print([event.value, 'B button'])






