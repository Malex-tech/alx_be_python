# finance_calculator.py

# Prompt the user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after one year with 5% simple interest
projected_savings = ((monthly_savings * 12) + (monthly_savings * 12 * 0.05))

# Display results as integers (whole numbers)
print("Your monthly savings are $" + str(int(monthly_savings)) + ".")
print("Projected savings after one year, with interest, is: $" + str(int(projected_savings)))