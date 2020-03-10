# What are lambda functions in Python?
* In Python, anonymous function is a function that is defined without a name.
* While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword
* This function can have any number of arguments but only one expression, which is evaluated and returned.
* One is free to use lambda functions wherever function objects are required.
```
f = lambda a: a*a
result = f(5)
print(result)   # 25
```
```
f = lambda a,b: a+b
result = f(5,6)
print(result)   # 11
```
## map()

map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
### Syntax :

> map(fun, iter)
```
def addition(n): 
	return n + n  
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

```
```
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 
```
## filter() 
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

### syntax:

> filter(function, sequence)
```
def fun(variable): 
	letters = ['a', 'e', 'i', 'o', 'u'] 
	if (variable in letters): 
		return True
	else: 
		return False
	       
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
	print(s) 
````
````
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13] 

# result contains odd numbers of the list 
result = filter(lambda x: x % 2, seq) 
print(list(result)) 

# result contains even numbers of the list 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 
```
