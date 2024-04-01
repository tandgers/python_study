from tkinter import *
from tkinter import messagebox
 
root = Tk()  # 新建一个窗口
 
btn01 = Button(root)  # 把一个button对象放到root窗口里面
btn01["text"] = "点我就送花"
 
btn01.pack()  # 调用布局管理器，把组件对象合理的放在窗口里面，pack压缩，把窗口变小了
 
 
def songhua(e):  # e就是事件对象
    messagebox.showinfo("Message", "送你一朵花")
    print("送你99朵玫瑰")
 
 
btn01.bind("<Button-1>", songhua)
root.mainloop()  # 调用组件的mainloop()方法，进入事件循环