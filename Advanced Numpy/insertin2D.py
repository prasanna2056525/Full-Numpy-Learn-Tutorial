import numpy as np 

arr =np.array([[10,20,30,40,50,60],
               [70,80,90,100,110,120]])

new_arr = np.insert(arr,1,[120,1,2,3,4,5],axis=0)

print(new_arr)
