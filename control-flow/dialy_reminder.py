# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a high priority task that requires immediate attention today!")
    
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium priority task that should be completed today.")
        else:
            print(f"'{task}' is a medium priority task. Consider completing it when possible.")
    
    case 'low':
        if time_bound == 'no':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")