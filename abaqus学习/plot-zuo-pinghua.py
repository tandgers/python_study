# 画变形后的结点散点图
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

order_zuo = [2,1,5,6,7,8,0,9,3,15,14,13,12,11,4,10,2] #结点顺序首尾为1点
Filename = ['0604-8']
# Filename = ['0604-8','0605-3','0605-6']


coords = np.load('C:/Temp/'+Filename[0]+'zuo_zuobiao.npy')
x=[]
y=[]
for j in order_zuo:
    x.append(coords[j,0])
    y.append(coords[j,1])

x = np.array(x)
y = np.array(y)


xnew = np.linspace(x.min(), x.max(), 300)
gfg = make_interp_spline(x, y, k=3)
y_new = gfg(xnew)
plt.plot(xnew, y_new)


# plt.plot(x,y)
for i in Filename:
    coords = np.load('C:/Temp/'+i+'zuo_zuobiao.npy')

plt.show()