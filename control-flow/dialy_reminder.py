# This script prompts the user for a single task and generates a customized reminder.
# It uses conditional statements, match/case (Python 3.10+), and loops for input validation.
# All code is executed procedurally without functions to meet the explicit request.

# --- 1. Prompt for a Single Task ---

# Ask the user to input a task description and save it into a task variable.
task = input("Enter your task: ")

# Initialize variables to ensure they are defined for static analysis
priority = ""
time_bound = ""

# Prompt for the task's priority (high, medium, low) and save it into a priority variable.
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ['high', 'medium', 'low']:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    
# In a time_bound variable, Ask if the task is time-bound (yes or no).
while True:
    # FIXED: Added '?' to the prompt string to match the example output exactly
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ['yes', 'no']:
        break
    print("Invalid response. Please enter 'yes' or 'no'.")


# --- 2. Process the Task and 3. Provide a Customized Reminder ---

# This variable will hold the final customized string.
final_reminder_message = ""

# Use a Match/Case statement to react differently based on the task's priority.
match priority:
    case 'high':
        # High Priority Logic
        # Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
        if time_bound == 'yes':
            # Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
            # A message should be 'that requires immediate attention today!'
            # Matches the EXACT Time-Bound Example Output:
            # Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
            final_reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            # High Priority, Non-Time-Bound
            final_reminder_message = f"Note: '{task}' is a high priority task. Plan time for this soon."
    
    case 'medium':
        # Medium Priority Logic
        if time_bound == 'yes':
            final_reminder_message = f"Reminder: '{task}' is a medium priority task that needs attention today."
        else:
            final_reminder_message = f"Note: '{task}' is a medium priority task. Complete when convenient."

    case 'low':
        # Low Priority Logic
        # Matches the EXACT Non-Time-Bound Example Output if not time-bound
        if time_bound == 'yes':
             final_reminder_message = f"Note: '{task}' is a low priority task, but it has a deadline. Complete when possible."
        else:
            # Matches the EXACT Non-Time-Bound Example Output:
            # Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
            final_reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

    case _:
        # Fallback case (should not be reached due to input validation loop)
        final_reminder_message = "ERROR: Could not determine task priority. Please re-run."


# Print the final customized reminder
print(final_reminder_message)
