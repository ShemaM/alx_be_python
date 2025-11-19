# daily_reminder.py

def main():
    # Prompt for a Single Task
    task = input("Enter your task: ").strip()

    priority = input("Priority (high/medium/low): ").strip().lower()

    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Normalize time_bound
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
        # Print the customized reminder
        print(reminder)
    else:
        reminder += "."
        # Print the customized reminder with note about free time
        print(reminder)

        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

        # Optional closing line to align with your closing sentence
        print("Well done on completing this project! Let the world hear about this milestone achieved.")

if __name__ == "__main__":
    main()