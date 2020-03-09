# EMI
def emi(p, r, t): 
    r = r/(12*100)  # for one month interest  
    t = t*12       # for one month period
    emi = (p*r*pow(1+r,t))/(pow(1+r,t)-1) 
    return emi

principal = 10896; 
rate = 12; 
time = 3; 
emi = emi(principal, rate, time); 
print("Monthly EMI is= ", emi)
