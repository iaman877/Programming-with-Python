# Python Function Argument

## Default Argument in Python
* Python Program arguments can have default values. We assign a default value to an argument using the assignment operator in python(=). 
* when we call a function without a value for an argument, its default value (as mentioned) is used.

### (1) Default Argument in Python

Python Program arguments can have default values. We assign a default value to an argument using the assignment operator in python(=).
```
def greeting(name='User'):
                print(f"Hello, {name}")
greeting('Aman Bhardwaj')
```
### (2).  Keyword Arguments

With keyword arguments in python, we can change the order of passing the arguments without any consequences. 

```
def divide(a,b):
                return a/b
a= divide(3,2)
print(a)

```
### (3) Python Arbitrary Arguments

You may not always know how many arguments you’ll get. In that case, you use an asterisk(*) before an argument name.

#### example 1

```
def fun(*names):
                for name in names:
                                print(name)
fun('Aman','Anshika','Aryan')  
```
#### output :- 

> Aman

> Anshika

> Aryan

#### example 2
```
def person(name, *data):
   print(name)
   print(data)
person('Aman',20,'Kanpur',70071)
```
#### output :-
> Aman

> (20, 'Kanpur', 70071)

#### example 3

```
def person(name, **data):
   print(name)
   print(data)
person('Aman',a = 20,b ='Kanpur',c = 70071)
```
#### output 
> Aman

> {'a': 20, 'b': 'Kanpur', 'c': 70071}


