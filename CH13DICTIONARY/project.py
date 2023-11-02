""""
Create a program that keeps record of total sales for an entire week.
User should enter the date from the keyboard
"""

days_of_the_week = [
    
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    
]  

sales_records = []
for day in days_of_the_week:
    prompt1 = f"Enter the sales for {day}:  "
    sales = int(input(prompt1))
      
    sale_record = {}
     
    sale_record["day"] = day
    sale_record["amount"] = sales 
    
    sales_records.append(sale_record)
    
print(sales_records)

total_sales = 0
for sale in sales_records:
    print(f"{sale['day']}  => ${sale['amount']}")
    total_sales = total_sales + sale["amount"]
    
print(f"The totls sales for the week is: ${total_sales}")
