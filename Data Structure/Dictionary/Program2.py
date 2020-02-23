# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ",Dict) 
 

# Adding elements one at a time 
Dict[0] = 'Internet'
Dict[2] = 'of'
Dict[3] = 'things'
print("\nDictionary after adding 3 elements: ",Dict) 


# Adding set of values  to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ",Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ",Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ",Dict) 
