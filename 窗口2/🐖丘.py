#IntVar() 要配合控件便使用
import tkinter as tk
from tkinter import *
import tkinter
import serial
import struct
import time
from PIL import Image,ImageTk
    

    # while True:
    #     list=[]
    #     for i in range(7):
    #         read = ser.read()
    #         list.append(read)
    #     print(list)
    #     # a=list[1][0] #a=97
    #     b=(list[1][0]-48)*100+(list[2][0]-48)*10+list[3][0]-48 #数字0 -48
    #     print(b)
if __name__=="__main__":
    try:
        ser = serial.Serial(port='COM4', baudrate=9600)
        
    except:
        print('cuole')
    top=tk.Tk()
    top.wm_title("测试")
    top.geometry('720x700')
    
    
    # cv = Canvas(top, bg='white')
    # cv.create_rectangle(10, 10, 200, 200)
    # cv.pack()
    im_root = ImageTk.PhotoImage(Image.open('1.jpg'))
    canvas_root = Canvas(top, width=500, height=400)#440 440
    # ==============================改娃娃头像🐖========================
    canvas_root.create_image(100, 320, image=im_root)#500  420龟  100 320丘
    # ==================================================================
    canvas_root.pack()

    var = tk.IntVar()	#保存为一个int类型的变量
    var.set(0)	#设置初始值
    count = 0	#通过计数来改变var值
    # Label(top, text= "测试" , font = ("黑体",100),fg = "red" , width = 100,height = 100).place(x = 20,y = 40,anchor = 'nw')  #12 2 play 20 40
    Label(top, text= "测试" , font = ("黑体",50),fg = "red" ).place()  
    # while(True):
    
    #     count += 1
    #     top.update()  #不断更新
    #     top.after(10) 
    #     if count % 50 == 0:
    #         var.set( var.get() + 1 )#变化的值，此处修改为你的变量
    #         # Label(top, text= str(var.get()) , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw') 
    #         Label(top, text= str(var.get()) , font = ("黑体",100),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw')
    while(True):
    

            top.update()  #不断更新
            top.after(100) #刚才是10
            list=[]
            for i in range(7):
                read = ser.read()
                list.append(read)
            # print(list)
            # a=list[1][0] #a=97
            b=(list[0][0]-48)*100000+(list[1][0]-48)*10000+(list[2][0]-48)*1000+(list[3][0]-48)*100+(list[5][0]-48)*10+list[6][0] #数字0 -48
            
            # print(b)
            # ===============b=100xxx 🐖改显示数值===============================
            c=int((b-100500-1650-210+1450)//65)
            
            if c<22:
                c=0
            # elif 0<c<=10:
            #     c=12
            # elif 0<c<=10:
            #     c=13
            # elif 10<c<=20:
            #     c=22
            # elif 20<c<=30:
            #     c=34
            # elif 30<c<=40:
            #     c=45
            # elif 40<c<=50:
            #     c=53
            # elif 50<c<=60:
            #     c=62
            # elif 60<c<=70:
            #     c=71
            # elif 70<c<=80:
            #     c=87
            # elif 80<c<=90:
            #     c=92
            # elif 90<c<=100:
            #     c=103
            # elif 100<c<=110:
            #     c=115
            elif c>122:
                c=122
            
            
            # ========================================================
            # var.set( var.get() + 1 )#变化的值，此处修改为你的变量
            # Label(top, text= str(var.get()) , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw') 
    # ======================================🐖可以改字体和显示的地方=======================================================================        
            Label(top, text= '下{}N'.format(c) , font = ("黑体",180),fg = 'red' , width = 12,height = 1).place(x=-370,y=400) #y=80
            # Label(top, text= '{}'.format(b) , font = ("字体",字数),fg = "颜色" , width = 12,height = 1).place(x=-475,y=400)
    # ===========================================================================================================================
    # top.mainloop() 



# ; -----------------------------------------------
# ; import tkinter as tk
# ; from tkinter import *
# ; import time
# ; if __name__=="__main__":

# ;     top=tk.Tk()
# ;     top.wm_title("测试")
# ;     top.geometry('500x300')
    
# ;     var = tk.StringVar()  #保存为一个string类型的变量
# ;     var.set("0")        #设置初始值
# ;     Label(top, text= "测试" , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 20,y = 40,anchor = 'nw') 
    
# ;     while(True):

# ;         time.sleep(1)
# ;         top.update()  #不断更新
# ;         top.after(10) 
# ;         var.set(chr(ord(var.get())+ 1))#为了展示处字符串变化的效果，煞费苦心，#变化的值，此处修改为你的变量
# ;         #我的只能停车收费系统用了车牌识别的API，可将不同车牌这一字符串展示界面
# ;         Label(top, text= var.get() , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw') 
        
# ;     top.mainloop() 
