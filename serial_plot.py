from random import random
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import keyboard
import serial

x = np.linspace(0, 10, 100)
y = np.zeros(np.size(x))
print(np.size(y))

plt.ion()
fig = plt.figure()
plt.ylim(0,65536)

ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')

####################################################################
ser = serial.Serial('COM8')
ser.baudrate = 115200
ser.timeout = 10 #specify timeout when using readline()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters
####################################################################
# while True:
#     if keyboard.is_pressed('\x1b'):
#         break
#     line=ser.readline()      #ascii
#     read_as_list = line.split(b'\n')
#     read_int= int(read_as_list[0])
#     print(read_int)

while True:
    if keyboard.is_pressed('\x1b'):
        break    
    line=ser.readline()      #ascii
    read_as_list = line.split(b'\n')
    read_int= int(read_as_list[0])

    y=np.delete(y,0)
    y=np.append(y, read_int)
    line1.set_ydata(y)

    fig.canvas.draw()
    fig.canvas.flush_events()
ser.close()
