# finance_calculator.py

# Prompt the user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings without interest
annual_savings = monthly_savings * 12

# Apply 5% simple interest
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results as whole numbers
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}")
