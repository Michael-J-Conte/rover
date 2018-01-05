#!/usr/bin/env python
import evdev 
import picamera


def buttoncheck():
    if event.type == 3: #check to see if event type is an absolute axis event
        if event.code == 3: 
            return [event.value, 'right analog']
        elif event.code == 16:
            return [event.value, 'D-Pad X']
        elif event.code == 17:
            return [event.value, 'D-Pad Y']
        elif event.code == 2:
            return [event.value, 'left trigger']
        elif event.code == 5:
            return [event.value, 'right trigger']
        elif event.code == 0:
            return [event.value, 'left analog']
        else:
            return ['NaN', 'none']
    
    elif event.type == 1:#check to see if event type is a button event
        if event.code == 307:
            return [event.value, 'X button']
        elif event.code == 308:
            return [event.value, 'Y button']
        elif event.code == 310:
            return [event.value, 'left bumper']
        elif event.code == 311:
            return [event.value, 'right bumper']
        elif event.code == 304:
            return [event.value, 'A button']
        elif event.code == 305:
            return [event.value, 'B button']
        else:
            return ['NaN', 'none']
    else:
        return ['NaN', 'none']



device = evdev.InputDevice("/dev/xbox1")
camera = picamera.PiCamera()
for event in device.read_loop():
    button = buttoncheck()
    if button[1] == 'A button':
        camera.capture('/home/pi/Workspace/Videos/test1.jpg')

    




