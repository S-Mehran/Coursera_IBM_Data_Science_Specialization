import numpy as np

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = np.array(a)
print(b)
print(type(b))
b_size = b.size
print(b_size)

print(b.ndim)
print(b.shape)
print(b[0,0:2])
print(b[1:3,2:4])

B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

C = np.dot(b, B)

print(C)

