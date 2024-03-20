import numpy as np 


## Array Function 





a = np.random.randint(1,100,15)
b = np.arange(24).reshape(6, 4)
print(a)

# isin 
print(np.isin(a, [10, 20, 30]))
# # flip 
print(np.flip(a))
print(np.flip(b, axis=1))

# put 
np.put(a, [0, 1], [110, 130])  # [0, 1] -> 0 index and 1 index replace to [110, 130]
print(a)


# delete 
c = np.delete(a, [0, 2, 3])  # [0, 2, 3] -> delete the 0, 2 and 3 index 
print(c)