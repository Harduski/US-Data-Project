import serial
import time

#init serial communication
ser = serial.Serial('COM1', 115200)


ser.write(b'1')
ser.write(b'6')
x = ser.readline()

y = ser.readline()

print(x)







