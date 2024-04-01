from tkinter import *
from tkinter import messagebox

global C

def jisuan(A,C):
    #shuru = input("input 常数C= ")
    #C = int(shuru)
    # 初始值
    # A = 61235275               # 游戏显示值
    # B = 1704649568      # 内存中的值，也是CE中搜索的值
    # C = 4253557641      # 常数

    ans1 = A*16384

    if(ans1 > 4294967295):
            # ans1大于FFFFFFFF(16进制)，产生溢出
        ans1_16jin = '{:x}'.format(ans1)
        ans1_1 = ans1>>32                       # 溢出的高位（10进制）
        ans2 = ans1_1<<32                       
        ans1_2 = '{:x}'.format(ans1_1)          # 溢出的高位（16进制）
        ans3 = ans1 - ans2                      # 得到低位（10进制）
        weiyihou = ans1_1 + ans3
        anss = '{:x}'.format(weiyihou) 
    else:
        weiyihou = ans1
    B = weiyihou ^ C
    C1 = C
    return B

def callback():
    C = int(entry1.get())
    A = int(entry2.get())
    B = jisuan(A,C)
    # entry3.config(text = "dd")
    strPath.set(B)
    # print(B)

# 创建验证函数，验证是否为数字
def checknumber1():
    data = entry1.get()
    if data.isdigit():
        return True
    else:
        messagebox.showinfo("提示","'"+ data+"'" "：不是数字")
        print(data, "：不是数字")
        entry1.delete(0,END)
        return False
    
def checknumber2():
    data = entry2.get()
    if data.isdigit():
        callback()
        return True
    else:
        messagebox.showinfo("提示","'"+ data+"'" "：不是数字")
        print(data, "：不是数字")
        entry2.delete(0,END)
        return False

root = Tk()

root.title('Eushully修改器（天结1）')

root.geometry('500x300+100+200')
# 500宽度  300高度   距屏幕左侧100像素 顶部200像素



# 新建文本标签
labe1 = Label(root,text="  C：")
labe2 = Label(root,text="  A：")
labe3 = Label(root,text="  B：")
# grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
labe1.grid(row=0)
labe2.grid(row=1)
labe3.grid(row=2)
# 创建动字符串
Dy_String1 = StringVar()
Dy_String2 = StringVar()
strPath = StringVar()
# 为上面的文本标签，创建3个输入框控件
entry1 = Entry(root,textvariable =Dy_String1,validate ="focusout",validatecommand=checknumber1)
entry2 = Entry(root,textvariable =Dy_String2,validate ="focusout",validatecommand=checknumber2)
entry3 = Entry(root,textvariable = strPath)  
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

# 使用按钮控件调用函数
b1 = Button(root, text="点击执行回调函数", command=callback)
b1.grid(row=1, column=2)



# bt.bind('<Button-1>', dianji)  # 绑定点击事件
root.mainloop()  # 进入事件循环
