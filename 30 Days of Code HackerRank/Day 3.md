# Task
Given an integer,n , perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of  6 to 20, print Weird
* If n is even and greater than 20, print Not Weird

## Sample Input 0
 3
## Sample Output 0
Weird

## Sample Input 1
24

## Sample Output 1
Not Weird

```
N = int(input())

if N % 2 != 0:
    print("Weird")
else:
    if N <= 5:
        print("Not Weird")
    elif N <= 20:
        print("Weird")
    else:
        print("Not Weird")


```
