# Programming-with-Python

 Variables


* Variables are containers for storing data values.
* Unlike other programming languages, Python has no command for declaring a variable.
* A variable is created the moment you first assign a value to it

Example :
```python
  x = 1234
  y = "Aman"
  print(x)
  print(y)
```



Variables do not need to be declared with any particular type and can even change type after they have been set.

```
x = 78   
x = "Illona" 
print(x)
```

String variables can be declared either by using single or double quotes:

```
x = "Aman"  // is the same as
x = 'Aman'
```

Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z,0-9,and _)
* Variable names are case-sensitive (age, Age and AGE are three different variables)


Assign Value to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example

```
x, y, z = "X", "Y", 5
print(x)
print(y)
print(z)
```

And you can assign the same value to multiple variables in one line:

```
Example
x = y = z = "O"
print(x)
print(y)
print(z)
```

The Python print statement is often used to output variables.

* To combine both text and a variable, Python uses the + character:

Example
```
x = "A"
print("Python is " + x)
```

* You can also use the + character to add a variable to another variable:

```
x = "life is "
y = "awesome"
z =  x + y
print(z)
```

* For numbers, the + character works as a mathematical operator:
```
x = 78
y = 98
print(x + y)
```
* If you try to combine a string and a number, Python will give you an error:

```
x = 20
y = "Aman"
print(x + y)
```
