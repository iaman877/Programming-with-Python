## Why python?

* Python is a general-purpose language, which means it can be used to build just about anything, which will be made easy with the right tools/libraries.
* Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing. Many developers have also used Python to build productivity tools, games, and desktop apps, so there are plenty of resources to help you learn how to do those as well.
* Python is an easy programming language for beginners to start out with

### 1. Data Science

* Python is the leading language of many data scientist. For years, academic scholars and private researchers were using the MATLAB language for scientific research but it all started to change with the release of Python numerical engines such as ‘Numpy’ and ‘Pandas’.
* python also deals with the tabular, matrix as well as statistical data and it even visualizes it with popular libraries such as ‘Matplotlib’ and ‘Seaborn

### 2. Scripting & Automation.

* This is a very useful capability that allows you to type in a program and to have it executed immediately in an interactive mode.
* The code is written in the form of scripts and get executed
* Machine reads and interprets the code
* Error checking is done during Runtime
* Once the code is checked, it can be used several times. So by automation, you can automate certain tasks in a program. 

### 3. Big Data

Python handles a lot of hassles of data. It supports parallel computing where you can use Python for Hadoop as well. In Python, you have a library called “Pydoop” and you can write a MapReduce program in Python and process data present in the HDFS cluster.

### 4. Computer Graphics

Python is largely used in small, large, online or offline projects. It is used to build GUI and desktop applications. It uses ‘Tkinter‘ library to provide fast & easy way to create applications.

### 5. Artificial Intelligence

 You can actually make a machine mimic the human brain which has the power to think, analyze and make decisions.
 Furthermore, libraries such as Keras and TensorFlow bring machine learning functionality into the mix. It gives the ability to learn without being explicitly programmed. Also, we have libraries such as openCvthat helps computer vision or image recognition.
 
### 6. Web Development

Python has an array of frameworks for developing websites. The popular frameworks are Django, Flask, Pylons etc. Since these frameworks are written in Python, its the core reason which makes the code a lot faster and stable. We can also perform web scraping where you can fetch details from any other websites. You will also be impressed as many websites such as Instagram, bit bucket, Pinterest are build on these frameworks only.

### 7. Portable & Extensible

* The portable and extensible properties of Python allow you to perform cross-language operations seamlessly. Python is supported by most platforms present in the industry today ranging from Windows to Linux to Macintosh, Solaris, Play station, among others.
* Python’s extensibility features allow you to integrate Java as well as .NET components. You can also invoke C and C++ libraries.

#### 8. Simple & Easy To Learn

* Python is Free & open source
* High-level
* Interpreted
* Blessed with large community


## Install python

* https://www.python.org/downloads/
* path? 
* In order to execute these files( javac java python (command names)), it must locate these files in path environment variables

 ## Variables

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

_Variable Names_


A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z,0-9,and _)
* Variable names are case-sensitive (age, Age and AGE are three different variables)


_Assign Value to Multiple Variables_
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
## Global Variables
 
 A variable declared outside of the function or in global scope is known as global variable. This means, global variable can be accessed inside or outside of the function.
 
 ```
 x = "aman"
def func():
  print("Python is " + x)
  
  func()
```
## Standard data types

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

```
* Text Type       ::	str
* Numeric Types   ::	int, float, complex
* Sequence Types  ::  list, tuple, range
* Mapping Type    ::  dict
* Set Types       ::	set, frozenset
* Boolean Type    ::	bool
* Binary Types    ::	 bytes, bytearray, memoryview
```
