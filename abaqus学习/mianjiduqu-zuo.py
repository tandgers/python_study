# 读取suidao-zuo的结点面积
import numpy as np

Filename = '0605-3'
coords = np.load('C:/Temp/'+Filename+'zuo_zuobiao.npy')

order_zuo = [2,1,5,6,7,8,0,9,3,15,14,13,12,11,4,10] #结点顺序

def mianji_zuo17(order,points):
    """返回多边形面积
    """
    area = 0
    q = points[order[-1]]
    for i in order:
        p = points[i]
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return abs(area / 2)

mianji = mianji_zuo17(order_zuo,coords)
print(mianji)

