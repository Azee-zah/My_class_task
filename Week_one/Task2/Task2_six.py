customers_name = input("What is your name: ")
Units_consumed = int(input("How many units do you use?"))
cost_per_unit = float(input("how much is a unit"))
date = "31-02-25"
Total_bill = Units_consumed * cost_per_unit
print(f"Name\t        {customers_name}\nYour_bills\t{Total_bill}\nDate       {date}")