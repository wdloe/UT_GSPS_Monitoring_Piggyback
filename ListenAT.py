import serial
serBarCode = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

while True:

    #read data from serial port
    serBarCode = serBarCode.readline()

    #if there is smth do smth
    if len(serBarCode) >= 1:
        print(dataBarCode.decode("utf-8"))
