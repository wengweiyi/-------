from tkinter import *
from PIL import Image,ImageTk

root = Tk()
#注该代码下须有对应的图片文件
im_root = ImageTk.PhotoImage(Image.open('1.jpg'))
canvas_root = Canvas(root, width=440, height=440)
canvas_root.create_image(220, 220, image=im_root)
canvas_root.pack()