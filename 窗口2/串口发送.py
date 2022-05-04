#-*-coding:UTF-8-*-
import serial    #导入serial库 
ser = serial.Serial('COM5', baudrate=57600)   #打开端口，每一秒返回一个消息 COM3 需要设置为自己的串口
#try模块用来结束循环（靠抛出异常）
try:
  while 1:
    act = input('请设置led灯(h亮l暗): ');
    print('act:',act)
 
    print('actzhuan:',act.encode())
    print(act.encode()[0])

    ser.write(act.encode());#写s字符  需要用 encode 进行编码
    
    # response = ser.readline();#用response读取端口的返回值
    # print(response);#进行打印
except Exception as e:
  print(e);
  ser.close();#抛出异常后关闭端口