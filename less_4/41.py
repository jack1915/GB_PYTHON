import numpy as np

data = np.arange(6).reshape((2, 3))
print("Original Arr")
print(data)

tMat = np.transpose(data)
print("Transposed Arr")
print(tMat)