# File handling
-------------------------------------------------------------------------------------------------------------------------
file is the name location on disk to store relative information, it is used to permantely stored data in a non-volitile memory(e.g Hard Disk)

In python , a file operation takes place in the fallowing order 

* open a file 
* read/write (perform operation)
* close the file 
-----------------------------------------------------------------------------------------------------------------------

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
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
```
