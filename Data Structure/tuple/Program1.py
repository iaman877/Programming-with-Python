# An empty tuple 
t1 = () 
print (t1)  #()
# Creating non-empty tuples 

tup = 'Internet', 'of','Things'
print(tup)    # ('Internet', 'of','Things')

# Another for doing the same 
tup = ('Internet', 'of','Things') 
print(tup)  # ('Internet', 'of','Things')

# Code for concatenating 2 tuples 

tuple1 = (0, 1, 2, 3) 
tuple2 = ('Internet', 'of','Things')  

# Concatenating above two 
print(tuple1 + tuple2)  # (0, 1, 2, 3, 'Internet', 'of','Things')

# Code for creating nested tuples 
tuple3 = (tuple1, tuple2) 
print(tuple3)         # (0, 1, 2, 3,) ('Internet', 'of','Things')

# Code to create a tuple with repetition 

tuple4 = ('Bhardwaj',)*3
print(tuple4)       # ('Bhardwaj','Bhardwaj','Bhardwaj')
