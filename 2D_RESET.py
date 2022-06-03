from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time

def changle1(angle):
    if angle > -31 and angle < 46:
        kit.servo[1].angle = 45 + angle
    elif angle < -30:
        kit.servo[1].angle = 0
    elif angle > 45:
        kit.servo[1].angle = 170
def changle2(angle):
    if angle > - 31 and angle < 46:
        kit.servo[2].angle = 45 + angle
    elif angle < -30:
        kit.servo[2].angle = 0
    elif angle > 45:
        kit.servo[2].angle = 170
def changle3(angle):
    if angle > -31 and angle < 46:
        kit.servo[3].angle = 45 + angle
    elif angle < -30:
        kit.servo[3].angle = 0
    elif angle > 45:
        kit.servo[3].angle = 170

changle1(0)
time.sleep(0.01)
changle2(3)
time.sleep(0.01)
changle3(0)