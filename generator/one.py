# generator function hai jo loop karne ka ek tarika, agar app for loop use karoge to data store ho gati hai 
# memory me lekin generator me data store nahi hoti memoery me 
# data science me bahut gayad used hota hai 
# generator me return function nahi hoti, yield function hoti hai 

# def generator():
#     yield "first function"
#     yield "second function"
#     yield "Last function"

# a = generator()
# # print(next(a))
# # print(next(a))
# # print(next(a))

# for i in a:
#     print(i)


# def generator():
#     for i in range(1, 10):
#         # print(i)
#         yield i


# a = generator()
# print(next(a))
# print(next(a))
# for j in a:
#     print(j)


# how to make loop using generator function 
# def generator(start, end):
#     for i in range(start, end):
#         yield i 


# for i in generator(1, 10):
#     print(i)





### List comprehension
# L = [i**2 for i in range(1, 10)]   # 1 se 10 ka range me square kar elment ka matlub 2 ka square 4, 3 ka square 9
# print(L)


# range(1, 10) generates a sequence of numbers from 1 up to (but not including) 10.
# i**2 calculates the square of each number in the range.
# The entire expression [i**2 for i in range(1, 10)] creates a list containing these squared values.



## Generator Expression

L = (i for i in range(1, 10))

for i in L:
    print(i)
