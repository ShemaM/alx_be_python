#Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
# finance_calculator.py
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

#Project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings *12* 0.05)  # 5% interest on savings per month
print("Your monthly savings are: $", monthly_savings)
print("Your projected savings after one year with 5% interest is: $", projected_savings)