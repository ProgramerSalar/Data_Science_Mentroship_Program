# case 1 if the file is not present 
#1. open the file
#2. Read/write the data 
#3. close the file 
 
# f = open('sample.txt','w')      # sample.txt is file name, w means write # open the file 
# f.write('hello world')          # write the file 
# f.close()

# if you close the file then write give the error I/O operation on closed file.
# f.write('hello hero')


# write a multiple lines in one file 
# f = open('sample.txt','w')
# f.write('hello hero')
# f.write('\nhow are you')
# f.close()



# case -2 
# if file is already present and then write 

# f = open('sample.txt','w')
# f.write('hello sanman khan')
# f.close()



# problem with write mode if you add the text,then before text are remove 
# f = open('sample.txt','a')  # append mode 
# f.write("\ni am manish")
# f.close()


# if you add the text to much 
# List = ['orem Ipsum is simply dum']
# f = open('sample.txt','w')  # append mode 
# f.writelines(List)
# f.close()



# how to read the content 
# f = open('sample.txt','r')  # append mode 
# r = f.read()  
# print(r)



# f = open('sample.txt','r')  # append mode 
# r = f.read(10)  # 10 is how much character read 
# print(r)


# how to read line by line 
# f = open('sample.txt','r')  # append mode 
# s = f.readline()  # read the first line 
# s2 = f.readline()  # read the second line 
# print(s)
# print(s2)
# f.close()


# you see output are give the gap 
# f = open('sample.txt','r')  # append mode 
# s = f.readline()  # read the first line 
# s2 = f.readline()  # read the second line 
# print(s, end='')   # it adds a newline character (\n) at the end by default. However, if you specify end='', it will suppress the newline character, ensuring that the next thing printed appears on the same line.
# print(s2)
# f.close()



# reading the entire lines 
# f = open('sample.txt','r')  # append mode 
# while f.readline() != '':
#     s=f.readline()
#     print(s, end='')
# f.close()



# with open('sample.txt', 'w') as f:
#     f.write('saru khan')


# write the line with using the range 
# big_list = ['hello world' for i in range(1000)]
# with open('sample.txt', 'w') as f:
#     a = f.writelines(big_list)
    

# with open('sample.txt', 'r') as f:
#     chunk_size = 10   # every 10 character 
#     while len(f.read(chunk_size)) > 0:           # chunk size is greater than 0
#         print(f.read(chunk_size), end='')   # print the chunk and skip the line 
        

with open('sample.txt', 'r') as f:
    s = f.read(10)
    s = f.tell()     # how many character read if you using the tell
    print(s)
    f.seek(0)  # again start the zero position of character 
    print(f.read(10))
    print(f.tell())