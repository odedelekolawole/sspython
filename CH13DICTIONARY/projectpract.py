days_of_the_week = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thurdays", "Friday", "Saturday"
]
sales_records = []
for day in days_of_the_week:
    sales_amount = int(input(f"Enter the sale for {day}:  "))
    sale_record = {}
    sale_record["day"] = day
    sale_record["amount"] = sales_amount
    sales_records.append(sale_record) 
print(sales_records)

total_sales = 0
for sales in sales_records:
    print(f"{sale_record['day']} => ${sale_record['amount']}")
    total_sales = total_sales + sales_amount
print(f"Total sale sale from {days_of_the_week[0]} to {days_of_the_week[-1]} is {total_sales}")