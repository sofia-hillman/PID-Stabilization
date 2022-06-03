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

    
def changeAngle(angle):
    if angle > -86 and angle < 86:
        kit.servo[0].angle = int(angle) + 85
    elif angle < -85:
        kit.servo[0].angle = 0
    elif angle > 85:
        kit.servo[0].angle = 170

def tilt(xs):
    
    if len(xs) > 2:
        p = np.mean(xs[-3:-1])
        
    else:
        p = xs[-1]
    
    #print('p')
    #print(p)
    
    if len(xs) > 49:
        i = np.mean(xs[-50:-1])
        
    else:
        i = 0
    
    #print('i')
    #print(i)
        
    if len(xs) > 19:
        d = np.mean(xs[-7:-5])-np.mean(xs[-3:-1])
    else:
        d = 0
    
    #print('d')
    #print(d)
    
    cp = 0.3
    
    ci = 0.005
    
    cd = -2
    
    angle = cp*p + ci*i + cd*d
    
    #print('----')
    #print(cp*p)
    #print(cd*d)
    #print(angle)
    
    return angle

def pid():
    
    xs = []
    
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
            
            xs += [155-x]
            
            angle = tilt(xs)
            
            changle(angle)
            time.sleep(sleepTime)
            
def changle(angle):
    if angle > -86 and angle < 86:
        kit.servo[0].angle = angle + 85
    elif angle < -85:
        kit.servo[0].angle = 0
    elif angle > 85:
        kit.servo[0].angle = 170

time.sleep(0.1)

pid()