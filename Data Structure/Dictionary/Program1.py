 
# Note – Keys in a dictionary doesn’t allows Polymorphism.
#  keys can’t be repeated and must be immutable.


# Creating a Dictionary  with Integer Keys
Dict = {1: 'internet', 2: 'of', 3: 'things'} 
print("\nDictionary with the use of Integer Keys: ",Dict) 


# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ",Dict) 
 

# Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}.

# Creating an empty Dictionary 
Dict = {} 
print("\nEmpty Dictionary: ") 


# Creating a Dictionary  with dict() method 
Dict = dict({1: 'internet', 2: 'of', 3: 'things'}) 
print("\nDictionary with the use of dict(): ",Dict) 


# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'IoT'), (2, 'CSF')]) 
print("\nDictionary with each item as a pair: ",Dict) 

# Creating a Nested Dictionary  as shown in the below image 
Dict = {1: 'Geeks', 2: 'For', 3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
print("\nDictionary with each item as a pair: ",Dict)

