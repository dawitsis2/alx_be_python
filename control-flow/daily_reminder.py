# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and provide a customized reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task."
    case "medium":
        reminder = f"'{task}' is a medium-priority task."
    case "low":
        reminder = f"'{task}' is a low-priority task."
    case _:
        reminder = f"'{task}' has an unrecognized priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(f"Reminder: {reminder}")
