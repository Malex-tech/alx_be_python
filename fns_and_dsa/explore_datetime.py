# explore_datetime.py

# Guidance:
# Start by importing the necessary components from the datetime module.
from datetime import datetime, timedelta

# Look into the datetime.now() function to get the current date and time.
# This function gets the current system date and time.

def display_current_datetime():
    # Save the current date inside a current_date variable
    current_date = datetime.now()

    # Format and print the current date and time in “YYYY-MM-DD HH:MM:SS”
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Use timedelta(days=number_of_days) to represent the duration to add to the current date.
    # Save the future date inside a future_date variable
    future_date = current_date + timedelta(days=days_to_add)

    # Print the future date in a format like “YYYY-MM-DD”
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date based on user input
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Remember, Python’s official documentation is an excellent resource
# for learning how to use the standard library modules.

if __name__ == "__main__":
    main()