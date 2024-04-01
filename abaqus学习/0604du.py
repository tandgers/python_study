#!/user/bin/python
# -* - coding:UTF-8 -*-
# 读取变形前后所有节点坐标，读取变形位移

import numpy as np# 可输出txt文件
from odbAccess import*# 打开odb的库
import sys
import os

# 计算多边形面积
def polygon_area(points):
    """
    返回多边形面积
    """
    area = 0
    q = points[-1]
    for p in points:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return abs(area / 2)

Filename = '0604-7'
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
np.savetxt(Filename+'_origin_coordinates.txt',coordinates_bending)

zengliangbu = 0
mianji.append(polygon_area(coordinates_bending))

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
    np.savetxt('DISP.txt',DISP)

    # 回弹前节点坐标+回弹变形=回弹后坐标
    temp_coordinates_bending=np.array(coordinates_bending)[:,0:2]
    temp_DISP=np.array(DISP)
    coordinates_springback=temp_coordinates_bending+temp_DISP
    # np.savetxt('coordinates_springback.txt',coordinates_springback)
    mianji.append(polygon_area(coordinates_springback))
    zengliangbu += 1

np.savetxt('coordinates_springback.txt',coordinates_springback)
np.save('coordinates_springback.npy',coordinates_springback)

b = []
for i in range(len(mianji)-1):
    b.append((mianji[i+1] - mianji[0])/mianji[0])
    if b[i]>-0.005:
        tar = i


print(mianji)
print(b)
print(tar)

odb.close