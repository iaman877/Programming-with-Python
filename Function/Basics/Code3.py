# count no of even and odd numbers
code :- 

def count(list):
   even = 0
   odd = 0
   for i in list:
      if i%2 == 0:
         even += 1
      else:
         odd += 1
   return even,odd

list = {20,25,14,19,24,28,47,26,40,50,70}
even,odd = count(list)
print(even)
print(odd)
