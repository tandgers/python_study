# 画变形后的结点散点图
import matplotlib.pyplot as plt
import numpy as np
# b = []
# for i in range(len(a)-1-300):
#     b.append((a[i+1] - a[0])/a[0])
# #plt.plot(a, linewidth=2)
# plt.plot(b, linewidth=2)

Filename = '0604-7'
coords = np.load('C:/Temp/'+Filename+'_after_coordinates.npy')
for i in range(len(coords[:,0])):

    plt.scatter(coords[i,0],coords[i,1])
plt.show()