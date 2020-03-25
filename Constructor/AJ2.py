class Computer :
    def __init__(self):
        self.name ="Aman"
        self.age = 20 
    def update(self):   # actally in bracket it is assining C1
        self.age = 30

c1 = Computer()
c2 = Computer()
c1.name = "Ram"
c1.age = 21
c1.update()
print(c1.name)  # Ram 
print(c1.age)   # 30
print(c2.age)   # 20

