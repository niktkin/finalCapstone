# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# Importing libraries and setting constants
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    """Registers a new user by taking username and password input from the user."""
    while True:
        new_username = input("New Username: ")

        # Checking if user already exists
        if new_username in username_password:
            print("User already exists")
        else:
            break
    
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    # Verifying passwords match
    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match.")


def add_task():
    """Adds a new task to the task list."""

    # Taking input for task details
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
 
    # Use Try Except to handle invalid format errors 
    while True:
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified")
        
        # Check if the due date is in the past
        if due_date_time.date() < date.today():
            print("Due date cannot be in the past. Please enter a valid due date.")
        else:
            break

    curr_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    """
    Displays all tasks in the task list.

    Tasks details included:
    title, assigned user, dates, completion status, and description.
    """
    print("\nAll Tasks:")
    for i, task in enumerate(task_list, start=1):
        print("\n" + "*" * 60)
        print(f"\nTask {i}:")
        print(f"\tTitle:\t\t{task['title']}")
        print(f"\tAssigned to:\t{task['username']}")
        print(f"\tDate Assigned:\t{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"\tDue Date:\t{task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"\tTask Completed:\t{'Yes' if task['completed'] else 'No'}")
        print(f"\tTask Description:\n\t{task['description']}\n")
        print("*" * 60 + "\n")


def view_mine(curr_user):
    """Displays tasks assigned to the current user."""
    print(f"\nTasks Assigned to {curr_user}:")

    # Filter tasks assigned to the current user
    user_tasks = [t for t in task_list if t['username'] == curr_user]

    for i, task in enumerate(user_tasks, start=1):
        print("\n" + "*" * 60)
        print(f"Task {i}:")
        print(f"\tTitle:\t\t{task['title']}")
        print(f"\tDate Assigned:\t{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"\tDue Date:\t{task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"\tTask Completed:\t{'Yes' if task['completed'] else 'No'}")
        print(f"\tTask Description:\n\t{task['description']}\n")
        print("*" * 60 + "\n")

    task_choice = input("\nEnter task number to view details or enter 'b' to return to main menu: ")
    if task_choice == 'b':
        return
    elif task_choice.isdigit():
        task_index = int(task_choice) - 1
        # Ensure input is valid and task is assigned to the current user
        if 0 <= task_index < len(task_list) and task_list[task_index]['username'] == curr_user:
            print_task_details(task_index)
            # User can mark task as complete or choose to edit it
            action = input("\nEnter 'c' to mark as complete, 'e' to edit, or any key to return: ").lower()
            if action == 'c':
                mark_as_complete(task_index)
            elif action == 'e':
                edit_task(task_index, curr_user)
    else:
        print("Invalid input. Please enter a valid task number or 'b' to return to the main menu.")


def print_task_details(task_index):
    """Prints details of a specific task."""

    # Retrieve and display task details
    t = task_list[task_index]
    print("\nTask Details:")
    print(f"Title: {t['title']}")
    print(f"Assigned to: {t['username']}")
    print(f"Date Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
    print(f"Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}")
    print(f"Task Description:\n{t['description']}")
    print(f"Completed: {'Yes' if t['completed'] else 'No'}")


def mark_as_complete(task_index):
    """Marks a task as complete."""

    # Retrieve task details    
    task = task_list[task_index]

    # Check if the tasks is not already marked as complete    
    if not task['completed']:
        task['completed'] = True
        # Update task list in the tasks.txt file
        with open("tasks.txt", "w") as task_file:
            task_file.write(tasks_to_string())
        print("Task marked as complete.")
    else:
        print("Task is already marked as complete.")


def edit_task(task_index, curr_user):
    """Edits details of a specific task."""

    # Retrieve task details
    task = task_list[task_index]

    # Check if the task is not already completed
    if not task['completed']:
        # Prompt user for new details
        new_assigned_user = input("Enter new assigned user's name or press enter to keep the same: ")
        if new_assigned_user:
            task['username'] = new_assigned_user
        new_due_date = input("Enter new due date (YYYY-MM-DD) or press enter to keep the same: ")
        if new_due_date:
            try:
                task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
            except ValueError:
                print("Invalid date format. Task due date not changed.")
        # Update task list in the tasks.txt file
        with open("tasks.txt", "w") as task_file:
            task_file.write(tasks_to_string())
        print("Task details updated.")
    else:
        print("Task cannot be edited as it is already marked as complete.")


def tasks_to_string():
    """Converts task list to a string format."""
    task_strings = []
    for t in task_list:
        task_strings.append(";".join([
            t['username'],
            t['title'],
            t['description'],
            t['due_date'].strftime(DATETIME_STRING_FORMAT),
            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            "Yes" if t['completed'] else "No"
        ]))
    return "\n".join(task_strings)


def generate_reports():
    """Generates two files (task_overview.txt & user_overview.txt) for reporting"""

    if logged_in != "admin":
        print("Only admin users are allowed to generate reports.")
        return

    # Use a variable to track if reports are successfully generated
    success_flag = True

    # Generate task overview report
    total_tasks = len(task_list)
    completed_tasks = sum(1 for t in task_list if t['completed'])
    incomplete_tasks = total_tasks - completed_tasks
    
    # Convert datetime objects to date objects for comparison
    today_date = date.today()

    # Fix the comparison
    overdue_tasks = sum(1 for t in task_list if not t['completed'] and t['due_date'].date() < today_date)

    percentage_incomplete = (incomplete_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    try:
        with open("task_overview.txt", "w") as report_file:
            report_file.write("Task Overview Report\n\n")
            report_file.write(f"Total number of tasks: {total_tasks}\n")
            report_file.write(f"Total number of completed tasks: {completed_tasks}\n")
            report_file.write(f"Total number of incomplete tasks: {incomplete_tasks}\n")
            report_file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
            report_file.write(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%\n")
            report_file.write(f"Percentage of overdue tasks: {percentage_overdue:.2f}%\n")
    except Exception as e:
        print(f"\nError generating task overview report: {e}")
        success_flag = False

    # Generate user overview report
    user_task_count = {username: 0 for username in username_password.keys()}
    user_completed_task_count = {username: 0 for username in username_password.keys()}
    user_overdue_task_count = {username: 0 for username in username_password.keys()}
    
    # Convert datetime objects to date objects for comparison
    today_date = date.today()

    for t in task_list:
        user_task_count[t['username']] += 1
        if t['completed']:
            user_completed_task_count[t['username']] += 1
        elif t['due_date'].date() < today_date:  # Convert due date to date object
            user_overdue_task_count[t['username']] += 1

    try:
        with open("user_overview.txt", "w") as report_file:
            report_file.write("User Overview Report\n\n")
            report_file.write(f"Total number of users: {len(username_password)}\n")
            report_file.write(f"Total number of tasks: {len(task_list)}\n")
            for username in username_password.keys():
                total_tasks_assigned = user_task_count[username]
                completed_tasks = user_completed_task_count[username]
                incomplete_tasks = total_tasks_assigned - completed_tasks
                overdue_tasks = user_overdue_task_count[username]
                percentage_assigned = (total_tasks_assigned / len(task_list)) * 100 if len(task_list) > 0 else 0
                percentage_completed = (completed_tasks / total_tasks_assigned) * 100 if total_tasks_assigned > 0 else 0
                percentage_incomplete = (incomplete_tasks / total_tasks_assigned) * 100 if total_tasks_assigned > 0 else 0
                percentage_overdue = (overdue_tasks / total_tasks_assigned) * 100 if total_tasks_assigned > 0 else 0
                report_file.write(f"\nUser: {username}\n")
                report_file.write(f"Total number of tasks assigned: {total_tasks_assigned}\n")
                report_file.write(f"Percentage of total tasks assigned: {percentage_assigned:.2f}%\n")
                report_file.write(f"Percentage of completed tasks: {percentage_completed:.2f}%\n")
                report_file.write(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%\n")
                report_file.write(f"Percentage of overdue tasks: {percentage_overdue:.2f}%\n")
    except Exception as e:
        print(f"\nError generating user overview report: {e}")
        success_flag = False

    # Print confirmation message only if both files were generated succesfully.
    if success_flag:
        print(f"\nReports generated successfully.")


def display_statistics():
    """Displays task statistics"""

    with open("task_overview.txt", "r") as task_report_file:
        task_report = task_report_file.read()

    with open("user_overview.txt", "r") as user_report_file:
        user_report = user_report_file.read()

    print("\nTask Overview Report:\n")
    print(task_report)
    print("\nUser Overview Report:\n")
    print(user_report)

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist.")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password.")
        continue
    else:
        print("Login Successful!")
        logged_in = True


#Main menu
while True:
    print()
    menu = input('''Select one of the following options:
r - Regster a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()
    
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(curr_user)
    elif menu == 'gr':
        generate_reports()
    elif menu == 'ds' and curr_user == 'admin': 
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice. Please try again.")