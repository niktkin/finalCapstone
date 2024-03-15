Project Name
Task Manager Application

Description
This project is a command-line task management application designed to facilitate task tracking and organization within a team. It allows users to register, add tasks, view tasks, generate reports, and display statistics.

Table of Contents
Setup
Usage
Registration
Adding Tasks
Viewing Tasks
Generating Reports
Displaying Statistics
Admin Access
Important Notes
File Structure
Support
Contributors
License
Setup

Installation: Ensure Python is installed on your system. Clone this repository to your local machine.

Environment Setup: Open the project folder in a Python development environment, preferably VS Code.

File Structure: Maintain the file structure as provided. Ensure the program is executed from its root directory.

Dependencies: No external dependencies are required beyond Python's standard library.

Usage
1. Registration
Run the program and select the option to register.
Enter a unique username and password when prompted.

2. Adding Tasks
After registration or login, add tasks to the system.
Provide task details such as assigned user, title, description, and due date.

3. Viewing Tasks
View all tasks or filter tasks assigned to specific users.
Task details include title, assigned user, dates, completion status, and description.

4. Generating Reports
Admin users can generate reports to gain insights into task distribution and completion.
Two reports are generated: task_overview.txt and user_overview.txt.

5. Displaying Statistics
Admin users can display task statistics directly from the generated reports.

6. Admin Access
Admin rights are granted using the predefined username (admin) and password (password).
Important Notes
User Credentials: Use provided username (admin) and password (password) for admin access.
Folder Structure: Execute the program from its root directory to avoid file path issues.
Datetime Format: Ensure dates are entered in the format YYYY-MM-DD.
File Structure
tasks.txt: Stores task data including assigned user, title, description, due date, assignment date, and completion status.
user.txt: Contains registered user credentials in the format username;password.
task_overview.txt: Generated report providing an overview of tasks.
user_overview.txt: Generated report offering insights into user-specific task statistics.

Contributors
Nikitas Michael (@niktkin)
