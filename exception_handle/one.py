
# with open('exception_handle/sample.txt', 'w') as f:
#     f.write('hello world')



try:
    with open('exception_handle1/sample.txt', 'w') as f:
        print(f.read())

except:
    print('file not found')
