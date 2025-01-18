import numpy as np

abc = np.array([1,2,3,4,5])
print(abc.ndim)
xyz = np.array([[1,2,3,4],[5,6,7,8]])
print(xyz.ndim)
print(xyz[1,3])
a = np.linspace(1,10,10)
print(np.arange(10,5,-1))
print(abc[1:4])
print(xyz[1:3,-4:-1])