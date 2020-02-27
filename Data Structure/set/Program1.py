#  Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.

# Python program to demonstrate  Creation of Set in Python 

set1 = set()  # Set Created
print("Intial blank Set: ",set1) 

# Creating a Set with the use of a String 
set2 = set("Aman_Bhardwaj") 
print("\nSet with the use of String: ",set2) 

# Creating a Set with the use of Constructor (Using object to Store String) 
String = 'Aman_Bhardwaj'
set3 = set(String) 
print("\nSet with the use of an Object: ",set3) 

# Creating a Set with the use of a List 
set4 = set(["Internet", "of", "thing"]) 
print("\nSet with the use of List: ",set4) 

# Creating a Set with a List of Numbers (Having duplicate values) 
set5 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\nSet with the use of Numbers: ",set5) 

# Creating a Set with a mixed type of values (Having numbers and strings) 
set6 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values",set6)

