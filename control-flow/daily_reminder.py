# Daily Reminder Script
# This script helps users manage their tasks with priority and time sensitivity

def get_task_details():
    # Get task details from user
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    # Generate and print reminder message based on priority and time sensitivity
    match priority:
        case "high":
            base_message = f"{task} is a high priority task"
            if time_bound == "yes":
                print(f"Reminder: {base_message} that requires immediate attention today!")
            else:
                print(f"Reminder: {base_message}. Please address this task as soon as possible.")
        
        case "medium":
            base_message = f"{task} is a medium priority task"
            if time_bound == "yes":
                print(f"Reminder: {base_message} that requires attention today!")
            else:
                print(f"Note: {base_message}. Consider completing it in the next few days.")
        
        case "low":
            base_message = f"{task} is a low priority task"
            if time_bound == "yes":
                print(f"Reminder: {base_message} that needs to be done today.")
            else:
                print(f"Note: {base_message}. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

def main():

    task, priority, time_bound = get_task_details()
    print()
    generate_reminder(task, priority, time_bound)

if __name__ == "__main__":
    main()