# daily_reminder.py (no def main)

# Prompt for a Single Task
task = input("Enter your task: ").strip()

priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
time_bound_flag = time_bound.startswith("y")

# Process the Task Based on Priority using match-case
reminder = ""

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unspecified priority"

# Modify the reminder if time-bound
if time_bound_flag:
    reminder += " that requires immediate attention today!"
    print(reminder)
else:
    reminder += "."
    print(reminder)
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

