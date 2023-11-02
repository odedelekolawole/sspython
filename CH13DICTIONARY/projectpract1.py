""""
Create a program that keeps record of total sales for an entire year.
User should enter the date from the keyboard
"""

months_in_the_year = [
    "Janumary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
]

sales_records = []
for month in months_in_the_year:
    sales_amount = int(input(f"Enter the sales for {month}: "))
    monthly_sales = {}
    monthly_sales["month"] = month
    monthly_sales["amount"] = sales_amount
    sales_records.append(monthly_sales)
print(sales_records)
yearly_sales = 0
for sale in months_in_the_year:
    print(f"{monthly_sales['month']} => ${monthly_sales['amount']}")
    yearly_sales = yearly_sales + sales_amount
print(f"The Yearly sales from {months_in_the_year[0]} to {months_in_the_year[-1]} is {yearly_sales}")