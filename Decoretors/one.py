


def my_decorator(func):
    def my_func(*args):
        print('hello world')
        func(*args)
    return my_func



@my_decorator
def hello(num):
    print('hi')
    print(num)

@my_decorator
def sum(a, b):
    print(a*b)


sum(2, 3)
hello(2)
