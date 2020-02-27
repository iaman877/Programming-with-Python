# Addition of elements in a Set 

## Creating a Set 
set1 = set() 
print("Intial blank Set: ",set1) 

##  Adding element and tuple to the Set 
set1.add(1) 
set1.add(2) 
set1.add((3,4)) 
print("\nSet after Addition of Three elements: ",set1) 

![2](https://user-images.githubusercontent.com/49730521/75463688-29dfc800-59ac-11ea-9a2e-b0fbd2d52b5d.PNG)

## Adding elements to the Set using Iterator

set1 = set() 
for i in range(1, 6): 
	set1.add(i) 
print("\nSet after Addition of elements from 1-5: ",set1) 
