# Working of open() function

file = open('Aman.txt', 'r') 
for each in file: 
	print (each)  # This will print every line one by one in the file 

# output 
Aman bhardwaj

upes

http
--------------------------------------------------------------------------------
# working with read() mode 
file = open ("file.text", "r") 
print(file.read ()) 

# Another way to read a file is to call a certain number of characters 
# print(file.read(5)) 

output
Aman Bhardwaj
AjTk
Live
