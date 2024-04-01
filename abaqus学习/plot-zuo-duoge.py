# 画变形后的结点散点图
import matplotlib.pyplot as plt
import numpy as np
order_zuo = [2,1,5,6,7,8,0,9,3,15,14,13,12,11,4,10] #结点顺序

Filename = ['0604-8','0605-3','0605-6']
for i in Filename:
    coords = np.load('C:/Temp/'+i+'zuo_zuobiao.npy')
    # for i in range(len(coords[:,0])):

    #     plt.scatter(coords[i,0],coords[i,1])
    # plt.show()

    for i in order_zuo:
        plt.scatter(coords[i,0],coords[i,1])
        plt.plot(coords[i,0],coords[i,1],linestyle='solid')
plt.show()