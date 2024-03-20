import numpy as np 


## Array Function 





m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])



a = np.union1d(m,n)  # unite the m and n array
# print(a)


b = np.intersect1d(m, n) # comman number in array m and array n
print(b)

c = np.setdiff1d(m,n)  # oo item jo n array me nahi jo m array me hai
print(c)

d = np.setxor1d(m, n) # comman number remove  in array m and array n || 
print(d)


e = np.in1d(m, 10)  # number 10 m array me hai ya nahi
print(e)