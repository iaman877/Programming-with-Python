# Python program to demonstrate accessing a element from a Dictionary 

# Creating a Dictionary 
Dict = {1: 'Internet', 'name': 'of', 3: 'things'} 

# accessing a element using key 
print("Accessing a element using key:"+Dict[1]+" "+Dict['name']+" "+Dict[3]) 

# There is also a method called get() that will also help in acessing the element from a dictionary.

# Creating a Dictionary 
print("Accessing a element using get():",Dict.get(3)) 
