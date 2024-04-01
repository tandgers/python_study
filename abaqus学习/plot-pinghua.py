import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 9, 1, 3, 5])

xnew = np.linspace(x.min(), x.max(), 300)
gfg = make_interp_spline(x, y, k=3)
y_new = gfg(xnew)
plt.plot(xnew, y_new)
plt.show()
