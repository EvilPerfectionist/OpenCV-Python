from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

# normal distribution center at x=0 and y=5
#x = np.random.randn(100000)
#y = np.random.randn(100000) + 10
x = [1, 2, 3, 2]
y = [1, 2, 3, 2]

plt.hist2d(x, y, bins=40, norm=LogNorm())
plt.colorbar()
plt.show()