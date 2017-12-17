import numpy as np

z = np.array([[1, 2], [3, 4], [5, 6]])
print(z)
print(z[0])
print(z[[0]])
print(z[[[0]]])
print(z[[[[0]]]])
print(z[[[[[0]]]]])

x = np.arange(3)
print(x)
print(x[0])
print(x[[0]])
print(x[[[0]]])
print(x[[[[0]]]])
print(x[[[[[0]]]]])
print(x[[True, True, False]])

label =  np.array([0, 0, 1])
labels =  np.array([[0], [0], [1]])
a = z[label==0]
b = z[labels.ravel()==0]
x = x.reshape((3, 1))
c = x[label==0]
d = x[labels==0]
print([0]==[0])
print(label)
print(labels)
print(a)
print(b)
print(c)
print(d)
print(label==0)
print(labels==0)