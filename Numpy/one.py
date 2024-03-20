

## Array Function 
import numpy as np 

#### Working with mathematical formulas ##### 
## Sigmoid 
def Sigmoid(array):
    return 1/(1 + np.exp((-array)))


a = np.arange(100)
print(Sigmoid(a))


## mse 
actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)

# print(actual)
# print(predicted)

def mse(actual, prdicted):
    return np.mean((actual - prdicted)**2)


print(mse(actual, predicted))