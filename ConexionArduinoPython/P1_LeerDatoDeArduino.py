
import serial as conexion

arduino = conexion.Serial(port= 'COM2', baudrate=9600, timeout=1000)

while True:
    v = arduino.readline().decode().replace("\n","")
    print(v)