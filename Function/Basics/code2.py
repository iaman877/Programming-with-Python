#-----------------updating  a variable -----------
def Update(x):
   x = 8
   print(x)   # 8

a = 10
Update(a)
print(a)    # 10

#-----------------updating  a variable----------------

def Update(list):
   list[1] = 25
   print(list)   #[10,25,30]

list = [10,20,30]
Update(list)
print(list)    #[10,25,30]
