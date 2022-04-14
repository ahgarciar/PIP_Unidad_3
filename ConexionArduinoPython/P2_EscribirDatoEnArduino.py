
import serial as conexion

arduino = conexion.Serial(port= 'COM2', baudrate=9600, timeout=1000)

arduino.write("1".encode())

import time as t
t.sleep(1)

arduino.write("0".encode())

import time as t
t.sleep(1)

arduino.write("1".encode())
