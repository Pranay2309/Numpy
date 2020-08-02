import numpy as p
l=[[1,2,3],[5,6,4]]
ar1=p.array(l)
print(ar1)
print(ar1.size)
print(ar1.dtype)
print(ar1.ndim)
print(ar1.shape)

ar2=p.empty((2,4),dtype=int)
print(ar2)