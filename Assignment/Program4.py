# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
            num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")
            

print ("Maximum is", largest)
print ("Minimum is", smallest)
