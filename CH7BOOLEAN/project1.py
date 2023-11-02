"""
Project
"""

"""
Income Tax Calculator
    Gross income less than 1,000: Tax = 5%
    Gross income less than 5,000 and greater than or equal to 1,000: Tax = 10%
    Gross income less than 10,000 and greater than or equal to 5,000: Tax = 15%
    Gross income greater than or equal to 10,000 = 20%
"""


gross_income = int(input("Enter your gross income:  "))
if gross_income < 1000:
    tax = 0.05 * gross_income
elif (gross_income >= 1000 ) and (gross_income < 5000 ):
    tax = 0.1 * gross_income
elif (gross_income >= 5000) and (gross_income < 10000):
    tax = 0.15 * gross_income
else:
    tax = 0.2 * gross_income
    
net_income = gross_income - tax

print(f"The gross Income is: ${gross_income}")
print(f"The tax is: {tax}")
print(f"Your net income is: ${net_income}")
    
