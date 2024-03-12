# A decorator in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it.
# This can happen only because python functions are 1st class citizens.

# def modify(func, num):
#     return func(num)

# def square(num):
#     return num ** 2

# a = modify(square, 2)
# print(a)



def my_decoretor(func):
    def my_function():
        print("*********")
        func()
        print("******")

    return my_function()


def hello():
    print('hello')


my_decoretor(hello)
