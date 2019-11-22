import numpy as np
array = np.array([[2,7,6],[9,5,1],[4,3,8]])
print(np.sum(array,axis=0))
print(np.sum(array,axis=1))
print(np.trace(array))
print(np.trace(np.fliplr(array)))
