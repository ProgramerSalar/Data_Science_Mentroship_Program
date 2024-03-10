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



f = open('sample.txt','r')  # append mode 
r = f.read(10)  # 10 is how much character read 
print(r)