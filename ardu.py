import serial 
from time import sleep

#The following line is for serial over GPIO
port = "/dev/cu.usbserial-0001"


ard = serial.Serial(port,9600,timeout=5)


while True:
    ard.flush()
    print("Iteration")
    ard.write(b"a")
    sleep(10)
    msg = ard.readline()
    print(msg)