# daily_reminder.py

# Ask for task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for handling priority levels (Python 3.10+)
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority level"

# Use if-statement to modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
    print(f"Reminder: {message}")
else:
    message += ". Consider completing it when you have free time."
    print(f"Note: {message}")