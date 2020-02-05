a = 'A string'
b = "A string"
b == a  # there is no difference between these strings
b == a
print('Single quoted string with " is no problem')
print("Double quoted string with ' is no problem")
print("Double quoted string containing \" is OK with backslash")
print('Backslash before "n", as in \n, inserts a new line character')
print('''This string literal
... has more than one
... line''')
a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])     # slicing Get the characters from position 2 to position 5 (not included)
#Negative Indexing : Use negative indexes to start the slice from the end of the string:
print(b[-5:-2])   # Get the characters from position 5 to position 1, starting the count from the end of the string
print(len(a))
print(a.strip()) # it is built-in methods & returns "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']
