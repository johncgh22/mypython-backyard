from socket import timeout
import serial
import time
import keyboard

ser = serial.Serial('COM3', 9600, timeout=0)
ser.flushInput()

while True:
    data = ser.readline()
    val = data[0:len(data)-1]
    print(data.decode('utf-8'))
    bufClear = ser.read(ser.inWaiting())
    time.sleep(0.25)

    if keyboard.is_pressed('q'):
        print("Adios")
        break

ser.close()