from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import numpy as np


pixy.init ()
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

def tilt(r):
    
    if len(r) > 4:
        p = np.mean(r[-3:-1])
        
    else:
        p = r[-1]
    
    if len(r) > 19:
        i = np.mean(r[-20:-1])
        
    else:
        i = 0

    if len(r) > 19:
        d = r[-5]-(r[-1])
    else:
        d = 0

    cp = .2
    
    ci = 0.003
    
    cd = -1.5
    
    angle = cp*p + ci*i + cd*d

    return angle

def pid():
    
    xs = []
    ys = []
    
    sleepTime = 0.001
    
    blocks = BlockArray(100)
    frame = 0
    while 1:
      count = pixy.ccc_get_blocks (100, blocks)

      if count > 0:
        frame = frame + 1
        for index in range (0, count):
            sig = blocks[index].m_signature
            x = blocks[index].m_x
            y = blocks[index].m_y
            
            xs += [x - 170]
            ys += [y - 130]
            
            r1 = [0.5*xs[i] - (np.sqrt(3)/2)*ys[i] for i in range(len(xs))]
            r2 = [-1*xs[i] for i in range(len(xs))]
            r3 = [0.5*xs[i] + (np.sqrt(3)/2)*ys[i] for i in range(len(xs))]            
            angle1 = tilt(r1)
            print(angle1)
            angle2 = tilt(r2)
            #print(angle2)
            angle3 = tilt(r3)
            #print(angle3)
            
            changle1(angle1)
            time.sleep(sleepTime)
            changle2(angle2)
            time.sleep(sleepTime)
            changle3(angle3)
            time.sleep(sleepTime)
            
def changle1(angle):
    if angle > -31 and angle < 46:
        kit.servo[1].angle = 45 + angle
    elif angle < -30:
        kit.servo[1].angle = 15
    elif angle > 45:
        kit.servo[1].angle = 90
def changle2(angle):
    if angle > - 31 and angle < 46:
        kit.servo[2].angle = 45 + angle
    elif angle < -30:
        kit.servo[2].angle = 15
    elif angle > 45:
        kit.servo[2].angle = 90
def changle3(angle):
    if angle > -31 and angle < 46:
        kit.servo[3].angle = 45 + angle
    elif angle < -30:
        kit.servo[3].angle = 15
    elif angle > 45:
        kit.servo[3].angle = 90


pid()