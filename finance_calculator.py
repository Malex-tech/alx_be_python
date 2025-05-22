# finance_calculator.py

# Prompt the user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings (12 months)
annual_savings = monthly_savings * 12

# Apply 5% annual interest
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")