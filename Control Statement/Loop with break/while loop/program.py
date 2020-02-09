counter = 0
while counter < 3:
    counter = counter + 1
    print("Inside loop",counter)
else:
    print("Inside else")
#-----------------------------------------------
n = 2
while n > 0 :
    n -= 1
    print(n)
#-----------------------------------------------
# Program to add natural numbers upto  sum = 1+2+3+...+n
n = 10
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    
print("The sum is", sum)
#-----------------------------------------------
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'
i = 0
while i < len(a):
    if a[i] == s :
        break
    i += 1
else:
     print(s, 'not found in list.')
#--------------------------------------------------------
if s in a:
    print(s, 'found in list.')
else:
    print(s, 'not found in list.')
#--------------------------------------------------------
# infinite lopp
while True:
     print('foo')
#--------------------------------------------------------
# one line while loop
n = 5
while n > 0: n -= 1; print(n)


