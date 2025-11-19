# This script prompts the user for a single task and generates a customized reminder.
# It uses conditional statements, match/case (Python 3.10+), and loops for input validation.

print("\n--- Task Reminder Generator ---")

# 1. Prompt for a Single Task
# Ask the user to input a task description and save it into a task variable.
task = input("Enter your task: ")

# 2. Prompt for Priority
# Prompt for the task's priority and save it into a priority variable.
# We prompt once at the top level to ensure static analysis finds the 'input' call easily.
priority = input("Priority (high/medium/low): ").lower().strip()

# Loop for validation (demonstrating loops)
while priority not in ['high', 'medium', 'low']:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    priority = input("Priority (high/medium/low): ").lower().strip()

# 3. Prompt for Time Sensitivity
# In a time_bound variable, Ask if the task is time-bound.
# Matches the EXACT screenshot prompt: "Is it time-bound? (yes/no): "
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Loop for validation
while time_bound not in ['yes', 'no']:
    print("Invalid response. Please enter 'yes' or 'no'.")
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()


# 4. Process the Task and Provide Reminder
# Use a Match Case statement to react differently based on the task's priority.

match priority:
    case 'high':
        # High Priority Logic
        # Within the Match Case, use an if statement to modify the reminder if the task is time-bound.
        if time_bound == 'yes':
            # Matches exact example: Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Plan time for this soon.")

    case 'medium':
        # Medium Priority Logic
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium priority task that needs attention today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Complete when convenient.")

    case 'low':
        # Low Priority Logic
        if time_bound == 'yes':
            print(f"Note: '{task}' is a low priority task, but it has a deadline. Complete when possible.")
        else:
            # Matches exact example: Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        print("ERROR: Could not determine task priority.")
