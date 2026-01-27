# ci-hackathon-3-group-1

# Introduction
This app was designed by Jonnie, Ree and Lewis. Our aim is to create a simple, functional task-management application that allows users to track, update, and remove tasks.
This project is built for educational purposes to demonstrate Django CRUD functionality and user interaction.

# Features


# User Stories

User Authentication & Accounts
Sign Up
- As a visitor, I want to create an account using my email/username and password, so that my todo lists are private and saved.
-  As a visitor, I want to see validation errors if my signup details are invalid, so I can fix them.
- As a visitor, I want to be prevented from signing up with an existing username/email, so accounts remain unique.

Log In / Log Out
- As a registered user, I want to log in with my credentials, so I can access my todo lists.
- As a logged-in user, I want to log out securely, so others cannot access my account.
- As a user, I want to be redirected to my dashboard after logging in, so I can start managing my todos immediately.

Session Management
- As a user, I want to stay logged in across page refreshes, so I don’t lose my session unexpectedly.
- As a user, I want to be logged out automatically when my session expires, for security.

User Dashboard
- As a logged-in user, I want to see a dashboard listing all my todo lists, so I can quickly navigate between them.
- As a user, I want to see an empty state message when I have no todo lists, so I know how to get started.    
Todo Lists Management
Create Todo Lists
- As a user, I want to create multiple todo lists, so I can organize tasks by category (e.g., Work, Personal).
- As a user, I want to give each todo list a title, so I can easily identify it.
View Todo Lists
- As a user, I want to open a specific todo list, so I can view its tasks.
- As a user, I want to see only my own todo lists, so my data remains private.

Update Todo Lists
- As a user, I want to rename a todo list, so I can change its purpose over time.

Delete Todo Lists
- As a user, I want to delete a todo list, so I can remove lists I no longer need.
- As a user, I want to be warned before deleting a todo list, so I don’t lose data accidentally.

Todo Items (Tasks)
Create Tasks
- As a user, I want to add tasks to a specific todo list, so I can track things I need to do.
- As a user, I want to give each task a title and optional description, so I know what needs to be done.
View Tasks
- As a user, I want to see all tasks within a todo list, so I can understand my workload.
- As a user, I want completed tasks to be visually distinct from incomplete ones, so I can quickly scan progress.

Update Tasks
- As a user, I want to edit a task’s title or description, so I can correct or refine it.
- As a user, I want to mark a task as completed, so I can track my progress.
- As a user, I want to mark a completed task as incomplete, in case I need to revisit it.

Delete Tasks
- As a user, I want to delete a task, so I can remove items that are no longer relevant.
Authorization and Data Protection
- As a user, I want to be prevented from accessing other users’ todo lists or tasks, so my data stays private.
- As a user, I want to receive a “not authorized” or “not found” message if I try to access data I don’t own.

Usability and Quality-of-Life
- As a user, I want clear success and error messages after actions (create, update, delete), so I know what happened.
- As a user, I want the app to work well on different screen sizes, so I can use it on desktop or mobile.
- As a user, I want forms to retain my input if submission fails, so I don’t have to retype everything.

Optional / Future Enhancements
- As a user, I want due dates on tasks, so I can prioritize my work.
- As a user, I want to reorder tasks within a list, so I can reflect priority.
- As a user, I want to archive completed tasks, so my lists stay clean.
- As a user, I want to search across my tasks, so I can find things quickly.

# Core Functionality
Allow users to create, edit, and delete tasks easily.
Provide status updates (e.g., "To Do", "In Progress", "Completed") for better task management.
Enable users to set and view due dates for their tasks.

# Wireframes
