file = open('file.txt', 'r')
content = file.read()  # This reads the content of the file
print(content)  # This prints the content
file.close()  # It's good practice to close the file after you're done

str=("hello , bhavesh here")
file = open('file','w')
content=file.write(str)
file.close

file=open("file.txt")
'''lines = file.readlines()
print(lines,type(lines))'''

line1=file.readline()
print(line1,type(line1))

line2=file.readline()
print(line2,type(line2))


str=("hello , bhavesh here")
file = open('file','a')  #append 
content=file.write(str)
file.close

