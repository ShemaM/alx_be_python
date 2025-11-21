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

# Build the core message using match-case
match priority:
    case "high":
        body = f"'{task}' is a high priority task"
    case "medium":
        body = f"'{task}' is a medium priority task"
    case "low":
        body = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Modify the message if the task is time-bound (yes)
if time_bound == "yes":
    # If it's low priority but time-bound, still emphasize immediate attention.
    body += " that requires immediate attention today!"

# Print the final reminder with the literal "Reminder:" prefix
print(f"Reminder: {body}")
