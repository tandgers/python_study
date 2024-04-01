# 画面积随增量步变化的图
import matplotlib.pyplot as plt
import numpy as np
Filename = '0604-7'
a = np.load('C:/Temp/'+Filename+'_mianji.npy')
b = []
for i in range(len(a)-1-500):
    b.append((a[i+1] - a[0])/a[0])
# plt.plot(a, linewidth=2)
plt.plot(b, linewidth=2)
plt.show()

