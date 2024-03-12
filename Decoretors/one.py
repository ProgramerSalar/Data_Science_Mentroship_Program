

def modify(func, num):
    return func(num)

def square(num):
    return num ** 2


a = modify(square, 2)
print(a)