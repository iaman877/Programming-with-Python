for i in range(1, 4): 
	print(i) 
else:                              # Executed because no break in for 
	print("No Break")
#---------------------------------------------------------------------------	
for j in range(1, 4): 
	print(j) 
	break
else:                               # Not executed as there is a break 
	print("No Break") 

