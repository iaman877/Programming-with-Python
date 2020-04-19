# Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

##  Input Format

There are  lines of numeric input:
* The first line has a double, metalCost (the cost of the meal before tax and tip).
* The second line has an integer, tipPercent (the percentage of  being added as tip).
* The third line has an integer, taxPercentage (the percentage of  being added as tax).
## Output Format

Print the total meal cost, where totalCost  is the rounded integer result of the entire bill metalCost( with added tax and tip)
## Sample Input

* 12.00
* 20
* 8
##  Sample Output

* 15

```
def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())

    # Write your calculation code here
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tax + tip))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")

```
