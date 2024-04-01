#!/user/bin/python
# -* - coding:UTF-8 -*-
# 读取变形前后所有节点坐标，读取变形位移

import numpy as np# 可输出txt文件
from odbAccess import*# 打开odb的库
import sys
import os

order_zuo = [2,1,5,6,7,8,0,9,3,15,14,13,12,11,4,10] #结点顺序
# 计算多边形面积
def mianji_zuo17(order,points):
    area = 0
    q = points[order[-1]]
    for i in order:
        p = points[i]
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return abs(area / 2)
# 输入odb文件名
Filename = '0605-6'
odb=openOdb(Filename+'.odb')# 读取odb

# 读取回弹前节点坐标
assembly=odb.rootAssembly# 读取odb.assembly
part=assembly.instances['PART-1-1']# 读取odb.assembly.instances



# txt回弹前坐标
mianji = []
coordinates_bending=[]
for node in part.nodeSets['SUIDAO-ZUO'].nodes:
    #coordinates_bending.append([node.label,node.coordinates[0],node.coordinates[1],node.coordinates[2]])
    coordinates_bending.append(node.coordinates)
# np.savetxt(Filename+'you_origin_coordinates.txt',coordinates_bending)

zengliangbu = 0
mianji.append(mianji_zuo17(order_zuo,coordinates_bending))

# 读取回弹变形
step1=odb.steps['Step-1']# 读取odb.steps
for lastFrame in step1.frames:
    


    magnitude = part.nodeSets['SUIDAO-ZUO']
    #lastFrame=step1.frames[-1]# 读取odb.step.frames
    displacement_last=lastFrame.fieldOutputs['U']# 读取odb.step.frames.fieldOutputs
    centerDisplacement = displacement_last.getSubset(region = magnitude)
    displacementValues_last=centerDisplacement.values# 读取odb.steps.frames.fieldOutputs.values

    # txt变形位移
    DISP = []
    for v in displacementValues_last:
        #DISP.append(v.dataDouble)
        DISP.append(v.data)
    #np.savetxt(Filename+'you_DISP.txt',DISP)

    # 回弹前节点坐标+回弹变形=回弹后坐标
    temp_coordinates_bending=np.array(coordinates_bending)[:,0:2]
    temp_DISP=np.array(DISP)
    coordinates_springback=temp_coordinates_bending+temp_DISP
    #np.savetxt('coordinates_springback.txt',coordinates_springback)
    mianji.append(mianji_zuo17(order_zuo,coordinates_springback))

    # 指定导出的增量步

    if lastFrame == step1.frames[11]:
        np.savetxt(Filename+'zuo_zuobiao.txt',coordinates_springback)
        np.save(Filename+'zuo_zuobiao.npy',coordinates_springback)
    zengliangbu += 1




b = []
for i in range(len(mianji)-1-330):
    b.append((mianji[i+1] - mianji[0])/mianji[0])
    if b[i]>-0.005:
        tar = i
np.save(Filename+'zuo_mianji.npy',mianji)

print(mianji)
print(b)
print('面积总个数：'+str(len(mianji))).decode('utf-8').encode('GB2312')
print('总增量步：'+str(len(step1.frames))).decode('utf-8').encode('GB2312')

odb.close