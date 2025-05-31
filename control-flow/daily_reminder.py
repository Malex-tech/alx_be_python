# daily_reminder.py

# Ensure you're using Python 3.10+ for match-case to work

while True:
    # Get user inputs
    task = input("Enter your task: ")
    priority = input("Priority (high, medium, low): ").lower()
    time_bound = input("Is it time-bound? (yes or no): ").lower()

    # Use match case for priority handling (requires Python 3.10+)
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.\n")
            continue  # loop back for correct input

    # Modify message based on time sensitivity
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print the customized reminder
    print("\nReminder:", message)
    break  # Exit after one successful task reminder
