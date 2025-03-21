import numpy as np

arr1d = np.array([1,2,3,4,5,6,7,8,9,10])
arrln = np.linspace(1,10,10)
arrnge = np.arange(10,1,-1)

arr_z = np.zeros([2,4],int)
arr_ones = np.ones([2,4])                   #BY DEF DATA TYPE FLOAT
xpt = arr1d.reshape([2,5])

h = arr1d  #ALIASING
hc = arrln.copy() #COPYING
empt = np.empty([2,4,3],int)

print(arr1d)
print(arrln)
print(arrnge)
print(arr_z)
print(arr_ones)
print(arr_z.ndim)                           #NO OF ROWS IN ARRAY
print(arr_z.shape)                          #NO OF ROWS AND COLUMNS IN ARRAY
print(xpt)
print()
print()
print(xpt.shape)
print(xpt+5)
print(hc.itemsize)
print(empt)