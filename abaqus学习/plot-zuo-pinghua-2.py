# 画变形后的结点散点图,并平滑连线
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.ticker import MultipleLocator, AutoLocator, FixedLocator

order_zuo = [2,1,5,6,7,8,0,9,3,15,14,13,12,11,4,10,2] #结点顺序首尾为1点

Filename = ['0604-8','0605-3','0605-6']

for i in Filename:
    coords = np.load('C:/Temp/'+i+'zuo_zuobiao.npy')
    x=[]
    y=[]
    for j in order_zuo:
        x.append(coords[j,0])
        y.append(coords[j,1])

    x = np.array(x)
    y = np.array(y)

    # 使用列表中的重复值绘制平滑曲线
    param = np.linspace(0, 1, x.size)
    spl = make_interp_spline(param, np.c_[x,y], k=2) #(1)
    xnew, y_smooth = spl(np.linspace(0, 1, x.size * 100)).T #(2)




    plt.plot(xnew, y_smooth,label=i)
    plt.scatter(x, y, c="r")

    # 设置坐标轴以固定间隔显示刻度
    x_major_locator=MultipleLocator(2)  #以每15显示
    y_major_locator=MultipleLocator(2)   #以每3显示
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    # 坐标轴显示比例一致，产生一个正方形图
    plt.axis('equal')



    # plt.plot(x,y)

plt.legend()
plt.show()