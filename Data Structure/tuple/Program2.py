#code to test that tuples are immutable 

tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)     #TypeError: 'tuple' object does not support item assignment

# code to test slicing 

tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:])      #(1, 2, 3)
print(tuple1[::-1])    #(3, 2, 1, 0)
print(tuple1[2:4])     #(2, 3)

# Code for deleting a tuple 

tuple3 = ( 0, 1) 
del tuple3 
print(tuple3)       # NameError: name 'tuple3' is not defined

# Code for printing the length of a tuple 

tuple2 = ('Aman', 'Bhardwaj') 
print(len(tuple2))          # 2

# Code for converting a list and a string into a tuple 

list1 = [0, 1, 2] 
print(tuple(list1))    #(0, 1, 2)
print(tuple('python'))  #('p', 'y', 't', 'h', 'o', 'n')



