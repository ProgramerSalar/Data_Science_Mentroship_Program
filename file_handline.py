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
f = open('sample.txt','w')
f.write('hello hero')
f.write('\nhow are you')
f.close()

