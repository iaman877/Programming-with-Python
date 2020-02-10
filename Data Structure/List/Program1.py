# Python program to demonstrate Creation of List Creating a List 

a = [2,8] 
print("List is : ",a) 

# Creating a List with  the use of a String 

List = ['Mr Rajeev Bhardwaj'] 
print("\nLList with String: ",List) 

# Creating a List with the use of multiple values

List = ["Aman", "Anshika", "Veena"] 
print("\nList containing multiple values: ",List) 
print(List[0])  
print(List[1]) 
print(List[2])

# Creating a Multi-Dimensional List  (By Nesting a list inside a List) 

List = [['IOT'], ['For'] , ['Smart'],['Cities']] 
print("\nMulti-Dimensional List: ",List) 
 
# Creating a List with the use of Numbers (Having duplicate values) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ",List) 

# Creating a List with Alpha_nnumeric value

List = [89, 2, 'Aman', 4.567, 'Branch is', .12, 'IOT'] 
print("\nList with the use of Mixed Values: ",List)

#---------------------------------------------------------------------------------
# Addition of Elements in the List 
List.append(1) 
print("\nList after Addition of Three elements: ",List) 

# Adding elements to the List using Iterator 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ",List)

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ",List) 

# Addition of List to a List 
List2 = ['Aman', 'Bhardwaj'] 
List.append(List2) 
print("\nList after Addition of a List: ",List)

#---------------------------------------------------------------------------------
# Python program to demonstrate Addition of elements in a List ( Creating a List)
# Important

List = [1,2,3,4] 
print("Initial List: ",List) 

# Addition of Element at specific Position (using Insert Method) 

List.insert(0, 'AmanDeep') 
List.insert(3, 12) 
print("\nList after Insert Operation: ",List) 

#----------------------------------------------------------------------------

# Python program to demonstrate Addition of elements in a List  Creating a List 
List = [1,2,3,4] 
print("Initial List: ",List)

# Addition of multiple elements to the List at the end (using Extend Method) 

List.extend([8, 'Be happy', 'Always']) 
print("\nList after Extend Operation: ",List) 

# Creating a Multi-Dimensional List  (By Nesting a list inside a List) 
List = [['Happy', 'For'] , ['Aman','harish']] 
print(List)
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][0],List[0][1],List[1][0],List[1][1]) 

#------------------------------------------------------------------------
# Python program to demonstrate Removal of elements in a List 

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

List.remove(5) 
List.remove(6) 
print("\nList after Removal : ",List) 


# Removing elements from List using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\n updated list : ",List) 
#----------------------------------------------------------------------------
List = [1,2,3,4,5] 

# Removing element from the pop() method 
List.pop() 
print("\nList after popping an element: ",List) 

List.pop(2)         # here 2 is index 
print("\nList after popping a specific element: ",List) 
