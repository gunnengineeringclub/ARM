import Tkinter as tk
from Tkinter import *
root = tk.Tk()
import serial
import math
import time
import threading







ser = serial.Serial('/dev/cu.usbserial-A70365JW', 38400, timeout=1)

def sendDegree(zero,one,two,three,four,five):
    message = str(zero)+","+str(one)+","+str(two)+","+str(three)+","+str(four)+","+str(five)+","
    ser.write(message)
    print(message)


# def open():

lastx = 0
lasty = 20
opengrab = False
movedup = False

rt = 550

def gt():
    global opengrab
    opengrab = not opengrab
    mv(lastx,lasty);



def mt():
    global movedup
    movedup = not movedup
    mv(lastx,lasty);

def quickchange():
    mv(0,8)
    time.sleep(0.1)
    mv(1,7)

def mv(xDistance, yDistance):

    print xDistance, yDistance

    global lastx
    global lasty
    lastx = xDistance
    lasty = yDistance

    b = 7.25
    a = 5.75
    # b = 18.0
    # a = 14.0

    originDist = math.sqrt(xDistance**2 + yDistance**2) + 0.00

    rotation = math.degrees(math.acos(yDistance / originDist))

    if(xDistance < 0):
        rotation *= -1;

    c = originDist

    cosA = (b**2 + c**2 - a**2) / (2*b*c)
    # print cosA
    angleA = math.degrees(math.acos(cosA))

    cosB = (c**2 + a**2 - b**2) / (2*c*a)
    angleB = math.degrees(math.acos(cosB))

    angleC = 180.0 - angleA - angleB;

    # print angleA,angleB,angleC
    # print (angleB / 90.0) * 500
    # print (angleC / 90.0) * 500

    grab = 1000
    if opengrab:
        grab = 0

    if movedup:
        angleB += 10

    p1 = math.ceil(((rotation / 90)*500 + 500)*100)/100
    p2 = math.ceil(((angleB / 90.0) * 500)*100)/100
    p3 = math.ceil(((angleC / 90.0) * 500)*100)/100
    p4 = math.ceil(((angleA / 90)*500 + 500)*100)/100
    p5 = math.ceil(rt*100)/100
    p6 = math.ceil(grab*100)/100



    sendDegree(p1,p2,p3,p4,p5,p6)
    # sendDegree(2,)


time.sleep(2)
mv(0,10)



def serialLog():
    while True:
        line = ser.readline()
        if(len(line) > 0):
            print(line)

thr = threading.Thread(target=serialLog)
thr.start() # will run "foo"


def draw():
    coords = [];
    with open("points.txt") as f:
        content = f.readlines()
        for i,val in enumerate(content):
            coords.append(val.split("\n")[0])

    print(coords)

    sleeptime = 3;

    for i in range(0,(len(coords)/4)):
        startx = float(coords[i*4])*-1
        starty = float(coords[i*4 + 1])
        endx = float(coords[i*4 + 2])*-1
        endy = float(coords[i*4 + 3])

        mt();
        time.sleep(sleeptime)
        mv(startx,starty)
        time.sleep(sleeptime)
        mt();
        time.sleep(sleeptime)
        mv(endx,endy)
        time.sleep(sleeptime)



mv(0,10)



def callback(event):
    mt()

def callback2(event):
    gt()

frame = Frame(root, width=1500, height=700)
frame.bind("<Button-1>", callback)
frame.bind("<Button-2>", callback2)
frame.pack()

lasttime = time.time()
def motion(event):
    global lasttime
    if time.time() > lasttime + 0.1:
        lasttime = time.time()
        x = ((event.x / 1300.0) * 14 - 7) * -1
        y = (event.y / 700.0)*10 + 3
        mv(x,y)

frame.bind('<Motion>', motion)
root.mainloop()
