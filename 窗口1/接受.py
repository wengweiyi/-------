import serial
import struct
import time
if __name__ == '__main__':
    try:
        ser = serial.Serial(port='COM3', baudrate=9600)
        
    except:
        print('cuole')

    while True:
        list=[]
        for i in range(7):
            read = ser.read()
            list.append(read)
        print(list)
        # a=list[1][0] #a=97
        b=(list[0][0]-48)*100+(list[2][0]-48)*10+list[3][0]-48 #数字0 -48
        print(b)
        # print('shuju:',a)
        # read=ser.read()
        # print(read)