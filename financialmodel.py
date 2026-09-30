income = float(input("Enter your monthly income: "))
savings = float(input("amount to save:"))
after_saving = income - savings
print("after_saving",after_saving)
food = float(input("how much is spent on food:"))
transport = float(input("how much is spent on transport:"))
school = float(input("how much is spent on school:"))
expenses = food + transport + school
remaining_income = after_saving - expenses
print("remaining_income",remaining_income)
expenses_percentage = (expenses / income)*100
print("expenses_percentage",round(expenses_percentage, 2),"%")






