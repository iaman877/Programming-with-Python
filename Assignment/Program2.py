# Write a Python program using functions to find the value of nPr and nCr without using inbuilt factorial() function.

import math
def nCr(n, r): 
	return (f1(n) / (f1(r) * f1(n - r))) 
def f1(n): 
	res = 1
	for i in range(2, n+1): 
		res = res * i 
	return res 
	
def f2(n): 
	if (n <= 1): 
		return 1
	return n * f2(n - 1) 
def nPr(n, r): 
	return math.floor(f2(n) /f2(n - r)) 
	
# Driver code 
n = 5
r = 3
print(int(nCr(n, r))) 
print(int(nPr(n, r)))
