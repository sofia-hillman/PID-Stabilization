from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time

def changeAngle(angle):
    if angle > -86 and angle < 86:
        kit.servo[0].angle = angle + 85
    elif angle < -85:
        kit.servo[0].angle = 0
    elif angle > 85:
        kit.servo[0].angle = 170
        
sleepTime = 0.01
time.sleep(sleepTime)
changeAngle(0)