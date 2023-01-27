#Tip Calculator - Day 02

bill = float(input("Enter your bill amount: $"))
no_of_people = int(input("How many people to split the bill: "))
tip = int(input("What percentage tip do you wanna give? 10, 12 or 15 ? "))
pay_per_person = (bill + (tip / 100) * bill) / no_of_people
print(f"Each should pay: $",round(pay_per_person,2))
