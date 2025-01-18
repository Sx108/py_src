import numpy as np
a=np.array([[2,3,4],[4,5,6],[7,8,9]])
b=np.concatenate([a,a],axis=1)
print (b)
xs = np.std(a,axis = 1,dtype= np.float64)
print (xs)