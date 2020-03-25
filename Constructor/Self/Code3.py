class Computer :
    def __init__(self):
        self.name ="Aman"
        self.age = 20 
    def campare(self,other):  # here self become C1
        if self.age == other.age:
            return True
        else:
            return False
            
c1 = Computer()
# c1.age = 30
c2 = Computer()
if c1.campare(c2):
    print("they are same")  # this will print 
else:
    print("they are not same")

-------------------------------------------------------------------------------------------------------
class Computer :
    def __init__(self):
        self.name ="Aman"
        self.age = 20 
    def campare(self,other):  # here self become C1
        if self.age == other.age:
            return True
        else:
            return False
 
c1 = Computer()
c1.age = 30
c2 = Computer()
if c1.campare(c2):
    print("they are same")
else:
    print("they are not same")

