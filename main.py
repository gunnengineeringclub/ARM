import serial
import math
import time

ser = serial.Serial('/dev/cu.usbserial-AL00WTYH', 9600)
# ser.write("1,1000");

def sendDegree(zero,one,two,three,four,five):
    message = str(zero)+","+str(one)+","+str(two)+","+str(three)+","+str(four)+","+str(five)
    ser.write(message)
    print(message)


# def open():



def moveDirectly(xDistance, yDistance):
    b = 18.0
    a = 14.0

    originDist = math.sqrt(xDistance**2 + yDistance**2) + 0.00

    rotation = math.degrees(math.acos(yDistance / originDist))

    if(xDistance < 0):
        rotation *= -1;

    c = originDist

    cosA = (b**2 + c**2 - a**2) / (2*b*c)
    print cosA
    angleA = math.degrees(math.acos(cosA))

    cosB = (c**2 + a**2 - b**2) / (2*c*a)
    angleB = math.degrees(math.acos(cosB))

    angleC = 180.0 - angleA - angleB;

    print angleA,angleB,angleC
    print (angleB / 90.0) * 1000
    print (angleC / 90.0) * 500



    sendDegree((rotation / 90)*500 + 500,(angleB / 90.0) * 1000,(angleC / 90.0) * 500,(angleA / 90)*500 + 500,600,1000)
    # sendDegree(2,)

currentx = 0
currenty = 20

time.sleep(2)
moveDirectly(currentx,currenty)


# sendDegree(1,1200)
