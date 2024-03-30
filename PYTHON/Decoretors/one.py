

n = int(input("Efnter Number"))
def my_decorator(func, *args):
    # func()
    return func(*args)

    

def hello(n):
    print(n)


my_decorator(hello, n)



# hello(2)