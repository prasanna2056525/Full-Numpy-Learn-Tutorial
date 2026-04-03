import numpy as np 

arr = np.array([1,2,-np.inf,4,np.nan,6])

cleaned_arr = np.isinf(arr)

print(cleaned_arr)

