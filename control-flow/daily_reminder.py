# daily_reminder.py

# Ask for the task
task = input("Enter your task: ")

# Keep asking until a valid priority is entered
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter high, medium, or low.")

# Keep asking until a valid time-bound response is entered
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter yes or no.")

# Process task using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Modify message if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"

# Print the final reminder
print(message)
