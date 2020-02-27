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
![3](https://user-images.githubusercontent.com/49730521/75464027-9c50a800-59ac-11ea-9764-05609ce5799b.PNG)

## Addition of elements to the Set using Update function 

set1 = set([ 4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\n using Update addition of number : ",set1)  

output :  using Update addition of number : {10, 11, 4, 5, (6, 7)}
