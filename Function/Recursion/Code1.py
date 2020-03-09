// Compound interest 

def compound_interest(principal, rate, years):
    return principal*(1 + rate)**years

def compound_interest_recursive(principal, rate, years):
    if years == 0:
        return principle
    else:
        return 



principal_str = input("Enter the principal ")
principal = int(principal_str)

rate_float = input("Enter the interest rate ")
rate = float(rate_float)

years_str = input("Enter the number of years ")
years = int(years_str)

print("Principal after", years,"year(s) is",compound_interest\(principal, rate, years))
