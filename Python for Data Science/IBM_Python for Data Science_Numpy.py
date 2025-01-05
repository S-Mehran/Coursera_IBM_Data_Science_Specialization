import numpy as np

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

c = type(b)
print(c)

a = np.array([10, 2, 30, 40,50])
a[1] = 20
print(a)


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])

b = np.array([10, 20, 30, 40, 50, 60, 70])

print(b.size)
print(b.ndim)
print(b.shape)

Mean = b.mean()
print(Mean)
St_Deviation = b.std()
print(St_Deviation)

max_value = b.max()
print(max_value)

min_value = b.min()
print(min_value)


c = np.array([-10, 201, 43, 94, 502])

c_max = c.max()
c_min = c.min()

sum_maxmin = c_max + c_min
print(sum_maxmin)


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr = arr1 + arr2
print(arr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])
arr = arr1*arr2
print(arr)

arr = np.dot(arr1, arr2)
print(arr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

arr = np.divide(arr1, arr2)
print(arr)

arr = np.array([1, 2, 3, -1]) 

print(arr + 5)

aaa = np.array([5,4])
print(np.linspace(5,4,num=6))



