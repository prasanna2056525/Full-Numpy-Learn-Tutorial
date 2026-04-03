import numpy as np 

arr1 =np.array([10,20,30,40,50,60])

arr2 =np.array([1,2,3,4,5,6])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)