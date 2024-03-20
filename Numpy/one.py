import numpy as np 


## Array Function 
# np.histogram
# Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.

# https://numpy.org/doc/stable/reference/generated/numpy.histogram.html




a = np.random.randint(1,100,15)
# print(a)

b = np.histogram(a, bins=[0, 50, 100])   # b/w 0 to 50 and 50 to 100 
print(b)
# output :-
# [ 5, 10]   # b/w 0 to 50 5 item and 50 to 100 10 item found 