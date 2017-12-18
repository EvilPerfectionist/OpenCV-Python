import numpy as np

x = np.array([[[0], [1], [2]]])
y = np.squeeze(x)
z = np.squeeze(x, axis=0)
a = np.squeeze(x, axis=2)
print(x.shape)
print(y)
print(y.shape)
print(z)
print(z.shape)
print(a)
print(a.shape)