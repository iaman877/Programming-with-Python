# File handling

file is the name location on disk to store relative information, it is used to permantely stored data in a non-volitile memory(e.g Hard Disk)

In python , a file operation takes place in the fallowing order 

* open a file 
* read/write (perform operation)
* close the file 


## Python File Read

Method 1 

```
obj = open("temp.txt",'r')
lines = obj.read()
print(lines)

```
Method 2

```
obj = open("temp.txt",'r')
for lines in obj:
    print(lines,end = "")
    
```
Method 3

3.1

```
obj = open("temp.txt",'r')
line = obj.readline()
print(line)

```
3.2

```
obj = open("temp.txt",'r')
line = obj.readline()
while line != '':
    print(line, end ='')
    line = obj.readline()
obj.close()

```
## Python File Write

Open the file "temp.txt" and append content to the file:
```
f = open("temp.txt", "a")
f.write("Now the file has more content!")
f.close()
```
Open the file "demofile3.txt" and overwrite the content:
```
f = open("demofile3.txt", "w")
f.write("Internet of things ")
f.close()
```
## Relative and absolute path 

* The absolute path start from the top most directory in the file System
* The Relative path start from current directory

```
import os
cwd = os.getcwd()
print(cwd)
```

## File tell() Method
The tell() method returns the current file position in a file stream.
### Syntax
> file.tell()

```
f = open("temp.txt", "r")
print(f.readline())
print(f.tell())
```
## File seek() Method
### Syntax

* f.seek(offset, from_what), where f is file pointer
* Parameters:
   (1) Offset: Number of postions to move forward
   (2) from_what: It defines point of reference.
* Returns: Does not return any value 


