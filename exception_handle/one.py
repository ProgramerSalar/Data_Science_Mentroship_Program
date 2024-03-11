
# with open('exception_handle/sample.txt', 'w') as f:
#     f.write('hello world')



try:
    m=5
    f = open('sample.txt','r')
    print(f.read())
    print(m)
    print(5/2)
    L = [1,2,3]
    L[100]


except FileNotFoundError:
    print('file not found')

except NameError:
    print('variable not found')

except ZeroDivisionError:
    print('cannot division by 0')

except Exception as e:
    print(e)