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

![map()](https://user-images.githubusercontent.com/49730521/76297102-44377100-62dd-11ea-8e3a-b21a5e9f1099.PNG)
