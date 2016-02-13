import serial
ser = serial.Serial('/dev/cu.usbserial-AL00WV7V', 9600)
ser.write("1,1000");

def sendDegree(servo,amount):
    ser.write(str(servo)+","+str(amount))
