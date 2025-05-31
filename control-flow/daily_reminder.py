# daily_reminder.py

# Ask for task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine reminder message based on priority
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"
else:
    reminder = f"'{task}' has an undefined priority level"

# Add time sensitivity to message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder += ". Consider completing it when you have free time."
    print(f"Note: {reminder}")
