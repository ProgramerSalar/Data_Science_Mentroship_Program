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
def generator(start, end):
    for i in range(start, end):
        yield i 


for i in generator(1, 10):
    print(i)


    