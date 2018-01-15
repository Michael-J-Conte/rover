#!/usr/bin/python

### Import Libraries ###
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit
import evdev
import picamera

mh = Adafruit_MotorHAT(addr=0x60)# create a default object, no changes to I2C address or frequency

### Function Abstractions ###
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def buttoncheck(): 
    if event.type == 3:
        if event.code == 4:
            return [event.value, 'right analog']
        elif event.code == 16:
            return [event.value, 'D-Pad X']
        elif event.code == 17:
            return [event.value, 'D-Pad Y']
        elif event.code == 2:
            return [event.value, 'left trigger']
        elif event.code == 5:
            return [event.value, 'right trigger']
        elif event.code == 1:
            return [event.value, 'left analog']
        else:
            return ['NaN', 'none']
    
    elif event.type == 1:
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



### Main Code ###
atexit.register(turnOffMotors)
rightmotor = mh.getMotor(2)
leftmotor = mh.getMotor(3)
device = evdev.InputDevice("/dev/xbox1")
for event in device.read_loop():
    button = buttoncheck()
    if button[1] == 'right analog':
        if button[0] < 0:
            rightmotor.run(Adafruit_MotorHAT.FORWARD)
            rightmotor.setSpeed(150)
        elif button[0] > 0:
            rightmotor.run(Adafruit_MotorHAT.BACKWARD)
            rightmotor.setSpeed(150)
    elif button[1] == 'left analog':
        if button[0] < 0:
            leftmotor.run(Adafruit_MotorHAT.FORWARD)
            leftmotor.setSpeed(150)
        elif button[0] > 0:
            leftmotor.run(Adafruit_MotorHAT.BACKWARD)
            leftmotor.setSpeed(150)
    elif button[1] == 'left trigger':
        rightmotor.run(Adafruit_MotorHAT.RELEASE)
        leftmotor.run(Adafruit_MotorHAT.RELEASE)
    elif button[1] == 'B button':
        quit()





### Code Graveyard ####

#myMotor.setSpeed(150) # set the speed to start, from 0 (off) to 255 (max speed)
#myMotor.run(Adafruit_MotorHAT.FORWARD) #turn on motor 
#myMotor.run(Adafruit_MotorHAT.RELEASE) #turn off motor

#while (True):
#    print("Forward! ")
#    myMotor.run(Adafruit_MotorHAT.FORWARD)
#
#    print("\tSpeed up...")
#    for i in range(255):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)

 #   print("\tSlow down...")
  #  for i in reversed(range(255)):
   #     myMotor.setSpeed(i)
    #    time.sleep(0.01)
#
#    print("Backward! ")
#    myMotor.run(Adafruit_MotorHAT.BACKWARD)

#    print("\tSpeed up...")
#    for i in range(255):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)

#    print("\tSlow down...")
#    for i in reversed(range(255)):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)

#    print("Release")
#    myMotor.run(Adafruit_MotorHAT.RELEASE)
#    time.sleep(1.0)




