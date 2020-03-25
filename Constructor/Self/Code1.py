class Computer :
    def __init__(self):
    pass         # we can't leave class empty
c1 = Computer()
c2 = Computer() 
print(id(c1))    # let x 
print(id(c2))    # let y != x
