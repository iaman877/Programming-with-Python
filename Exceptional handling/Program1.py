# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
try:
  print(x)
except NameError:
  print("Variable isnot defined")
except:
  print("Something not good ")
 #-------------------------------------------------------------------------------------------------------------------------
 # Use of else
 
 try:
  print("Hello world ")
except:
  print("Something went very  wrong")
else:
  print("everthing  went good ")
#----------------------------------------------------------------------------------------------------------------------------
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something is  wrong")
finally:
  print("finally call ")
 #----------------------------------------------------------------------------------------------------------------------------
 #To throw (or raise) an exception, use the raise keyword.
 x = -1
if x < 0:
  raise Exception("Sorry, number  numbers below zero")
 #----------------------------------------------
 y = "hello"
if not type(y) is int:
  raise TypeError("Only integers are allowed ")
 #----------------------------------------------------------------------------------------------------------------
# Program to depict Raising Exception 
try: 
	raise NameError("Hi there")       # Raise Error 
except NameError: 
	print("An exception")
	raise # To determine whether the exception was raised or not 
#-----------------------------------------------------------------------------------------------------------------
try: 
	k = 5//0 
	print(k) 
except ZeroDivisionError: 
	print("Can't divide by zero") 
	
finally: 
	print('This is always executed') 

