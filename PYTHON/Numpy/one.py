import numpy as np 


## Array Function 

a = np.random.randint(0, 100, 15)
print(a)

b = np.clip(a,a_min=25,a_max=75)   # a array me minimum value 25 or max value 75 hogi
print(b)

