# TickIt - A Task Management Django Application

## Introduction

This app was designed by Jonnie, Ree and Lewis. Our aim is to create a simple, functional task-management application that allows users to track, update, and remove tasks.
This project is built for educational purposes to demonstrate Django CRUD functionality and user interaction.

### Important Links

-   [GitHub Repository](https://github.com/lewis1190/ci-hackathon-3-group-1/tree/main)
-   [GitHub Project Board](https://github.com/users/lewis1190/projects/10)
-   [Deployed Application](https://ci-tickit-3981b641748d.herokuapp.com/)
-   [Project Presentation](https://docs.google.com/presentation/d/1d4toofZC3AVs5WGB6zzu-sgqvpaVyhCZ7lY1ciGarYk/edit?slide=id.g2b6f9610e6e_0_93#slide=id.g2b6f9610e6e_0_93)

## Features

- User Authentication: Sign up, log in, and log out functionality using `django-allauth`.

- Todo List Management: Create, read, update, and delete TODO lists.

- Task Management: Add, edit, mark as complete/incomplete, and delete tasks within each TODO list.

- Responsive Design: Mobile-friendly interface using Bootstrap 5.

- Custom Login UI to separate the login experience from the default allauth templates.

## Future Enhancements

Given more time to develop this project, we would implement the following:

- Provide status updates (e.g., "To Do", "In Progress", "Completed") for better task management.

- Enable users to set and view due dates for their tasks.

- Better responsive behavior, specifically for smaller screen sizes.

- Implement drag-and-drop functionality to reorder tasks within a list.

- Sharing lists with other users, allowing collaborative task management on select lists.

- Removal of ALL inline styles, replacing them with proper CSS classes in dedicated CSS files, imported per-template to minimize conflicts.

## Screenshots

![Dashboard Screenshot](./report_docs/screenshots/1.png)
*Screenshot of the main dashboard showing an overview of tasks and lists.*

![Deleting List Screenshot](./report_docs/screenshots/2.png)
*Screenshot showing the process of deleting a TODO list.*

![Sign Out Screenshot](./report_docs/screenshots/3.png)
*Screenshot showing the user signing out of the application.*

![Sign In Screenshot](./report_docs/screenshots/4.png)
*Screenshot of the custom sign-in page.*

## Planning

### Project Management and Methodology

Due to the very small timescale of this hackathon (3 days), we opted for a compressed, aggressive form of the Agile methodology. We created a project board on GitHub to track tasks and progress, using columns for "To Do", "In Progress", "In Review", and "Done".

![GitHub Project Board Screenshot](./report_docs/project_board.png)\
*Screenshot of the GitHub project board used. State of the board is from the end of the hackathon.*

Each day was planned with a specific goal, equivalent to what would normally be a fortnightly sprint:

- Day 1: Planning, preparation, setting up the repo, Github project and categorizing user stories.

- Day 2: Coding. Should have CRUD functionality for everything MVP by the end of the day. Project should be near-completion, except for testing, responsiveness improvements and bug fixing.

- Day 3: Testing, bug fixing, final deploys, report writing.

For communication, we used a Discord server to have discussion, share ideas and coordinate in real-time. We held brief daily stand-up meetings to discuss progress, challenges, and next steps.

![Discord Server Screenshot](./report_docs/discord.png)\
*Screenshot of the Discord server used.*

### User Stories

Below is a copy of our initial user stories that we created to guide the development of this project. These were noted, assigned and prioritized in the GitHub project board. Prioritization was done via the MoSCoW method (Must have, Should have, Could have, Won't have).

User Authentication & Accounts
Sign Up

-   As a visitor, I want to create an account using my email/username and password, so that my todo lists are private and saved.
-   As a visitor, I want to see validation errors if my signup details are invalid, so I can fix them.
-   As a visitor, I want to be prevented from signing up with an existing username/email, so accounts remain unique.

Log In / Log Out

-   As a registered user, I want to log in with my credentials, so I can access my todo lists.
-   As a logged-in user, I want to log out securely, so others cannot access my account.
-   As a user, I want to be redirected to my dashboard after logging in, so I can start managing my todos immediately.

Session Management

-   As a user, I want to stay logged in across page refreshes, so I don’t lose my session unexpectedly.
-   As a user, I want to be logged out automatically when my session expires, for security.

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

-   As a user, I want to rename a todo list, so I can change its purpose over time.

Delete Todo Lists

-   As a user, I want to delete a todo list, so I can remove lists I no longer need.
-   As a user, I want to be warned before deleting a todo list, so I don’t lose data accidentally.

Todo Items (Tasks)
Create Tasks

- As a user, I want to add tasks to a specific todo list, so I can track things I need to do.
- As a user, I want to give each task a title and optional description, so I know what needs to be done.
View Tasks
- As a user, I want to see all tasks within a todo list, so I can understand my workload.
- As a user, I want completed tasks to be visually distinct from incomplete ones, so I can quickly scan progress.

Update Tasks

-   As a user, I want to edit a task’s title or description, so I can correct or refine it.
-   As a user, I want to mark a task as completed, so I can track my progress.
-   As a user, I want to mark a completed task as incomplete, in case I need to revisit it.

Delete Tasks

- As a user, I want to delete a task, so I can remove items that are no longer relevant.
Authorization and Data Protection
- As a user, I want to be prevented from accessing other users’ todo lists or tasks, so my data stays private.
- As a user, I want to receive a “not authorized” or “not found” message if I try to access data I don’t own.

Usability and Quality-of-Life

-   As a user, I want clear success and error messages after actions (create, update, delete), so I know what happened.
-   As a user, I want the app to work well on different screen sizes, so I can use it on desktop or mobile.
-   As a user, I want forms to retain my input if submission fails, so I don’t have to retype everything.

Optional / Future Enhancements

-   As a user, I want due dates on tasks, so I can prioritize my work.
-   As a user, I want to reorder tasks within a list, so I can reflect priority.
-   As a user, I want to archive completed tasks, so my lists stay clean.
-   As a user, I want to search across my tasks, so I can find things quickly.

### Wireframes

We used Balsamiq web to create wireframes for the main pages of the application. We used Balsamiq's AI features to help speed up the wireframing process, given the tight deadline for the hackathon.

![Wireframe - Login](./report_docs/wireframes/1.png)\
*Wireframe of the Login Screen.*

![Wireframe - View Tasks](./report_docs/wireframes/2.png)\
*Wireframe of the Main Dashboard Screen.*

![Wireframe - Add New Task](./report_docs/wireframes/3.png)\
*Wireframe of the Add New Task Screen.*

![Wireframe - Edit Task](./report_docs/wireframes/4.png)\
*Wireframe of the Edit Task Screen.*

## Testing

To test this application, we focused on automated unit tests for the views. Below is a full table of all unit tests currently running, and their status as of the latest production deploy on 29/01/2026.

### home/test_views.py

| Test Function Name | Status |
| ----------- | -------- |
| test_home_view_requires_login | PASS |
| test_home_view_loads_with_login | PASS |
| test_home_view_contains_user_lists | PASS |
| test_home_view_does_not_show_other_users_lists | PASS |
| test_home_view_sets_current_list_to_first | PASS |
| test_home_view_with_selected_list_id | PASS |
| test_home_view_with_invalid_list_id | PASS |
| test_home_view_separates_completed_and_incomplete_items | PASS |
| test_home_view_no_lists_for_new_user | PASS |
| test_create_todo_list_requires_login | PASS |
| test_create_todo_list_requires_post | PASS |
| test_create_todo_list_success | PASS |
| test_create_todo_list_without_description | PASS |
| test_create_todo_list_without_title | PASS |
| test_create_todo_list_with_whitespace_title | PASS |
| test_add_todo_item_requires_login | PASS |
| test_add_todo_item_requires_post | PASS |
| test_add_todo_item_success | PASS |
| test_add_todo_item_without_list_id | PASS |
| test_add_todo_item_without_text | PASS |
| test_add_todo_item_with_whitespace_text | PASS |
| test_add_todo_item_with_nonexistent_list | PASS |
| test_add_todo_item_to_other_users_list | PASS |
| test_add_todo_item_redirects_with_list_id | PASS |
| test_edit_todo_item_requires_login | PASS |
| test_edit_todo_item_requires_post | PASS |
| test_edit_todo_item_success | PASS |
| test_edit_todo_item_without_text | PASS |
| test_edit_todo_item_other_user_forbidden | PASS |
| test_edit_todo_item_nonexistent | PASS |
| test_delete_todo_item_requires_login | PASS |
| test_delete_todo_item_requires_post | PASS |
| test_delete_todo_item_success | PASS |
| test_delete_todo_item_other_user_forbidden | PASS |
| test_delete_todo_item_nonexistent | PASS |
| test_toggle_todo_item_requires_login | PASS |
| test_toggle_todo_item_requires_post | PASS |
| test_toggle_todo_item_incomplete_to_complete | PASS |
| test_toggle_todo_item_complete_to_incomplete | PASS |
| test_toggle_todo_item_other_user_forbidden | PASS |
| test_toggle_todo_item_nonexistent | PASS |
| test_clear_completed_tasks_requires_login | PASS |
| test_clear_completed_tasks_requires_post | PASS |
| test_clear_completed_tasks_success | PASS |
| test_clear_completed_tasks_no_completed | PASS |
| test_clear_completed_tasks_other_user_forbidden | PASS |
| test_clear_completed_tasks_nonexistent_list | PASS |
| test_clear_completed_tasks_without_list_id | PASS |
| test_rename_todo_list_requires_login | PASS |
| test_rename_todo_list_requires_post | PASS |
| test_rename_todo_list_success | PASS |
| test_rename_todo_list_without_title | PASS |
| test_rename_todo_list_with_whitespace_title | PASS |
| test_rename_todo_list_other_user_forbidden | PASS |
| test_rename_todo_list_nonexistent | PASS |
| test_delete_todo_list_requires_login | PASS |
| test_delete_todo_list_requires_post | PASS |
| test_delete_todo_list_success | PASS |
| test_delete_todo_list_cascades_items | PASS |
| test_delete_todo_list_other_user_forbidden | PASS |
| test_delete_todo_list_nonexistent | PASS |

## How We Used AI in This Project

### Scoping and Discovery of User Stories

Whilst planning the project in Discord, we came up with a short list of user stories. To sanity-check our stories, as well as find any others that we might have missed, we fed our project spec to ChatGPT and requested any user stories that it we may have missed.

We also used it to automate the Markdown formatting of our user stories for easy copy-pasting into the GitHub project board.

![Markdown Formatting Assistance from ChatGPT](./report_docs/ai_section/stories.png)\
*Screenshot showing how ChatGPT helped format our user stories into Markdown for easy copy-pasting.*

### Mockups and Wireframes

The web version of Balsamiq has an AI assistant that can generate wireframes based on text prompts. We used this feature to quickly generate wireframes for the main pages of our application, which we then refined manually.

Meanwhile, we also used ChatGPT to create image-only mockups of our site, given the context of the user stories. As you can see, the image generated by ChatGPT ended up quite close to our final project!

![Mockup Generated by ChatGPT](./report_docs/ai_section/mockup.png)\
*Mockup of the main dashboard page, generated by ChatGPT based on our user stories.*

### Learning Unfamiliar Code and Functions

When working with other team members, or using AI to assist with code creation, there's always the chance of coming across unfamiliar code snippets or functions.

When this happened, CoPilot was used to provide explanations and context for these snippets, helping team members understand their purpose and how to use them effectively.

Once code was explained, it sometimes resulted in the re-implementation of a function, due to better understanding of its purpose.

![Code Explanation from CoPilot](./report_docs/ai_section/learning.png)\
*Screenshot showing how CoPilot helped explain an unfamiliar code snippet.*

### Debugging Unit Tests

When working with a comprehensive amount of unit tests, it's inevitable that some tests will fail during development. Again, CoPilot was used to help debug these tests by providing insights into why a test might be failing, and suggesting whether the **test** or the **code being tested** needed to be adjusted.

![Unit Test Debugging with CoPilot](./report_docs/ai_section/unit_testing_help.png)\
*Screenshot showing how CoPilot helped debug a failing unit test.*

## Installation & Setup Instructions

Follow these steps to set up and run this Django project on a new machine.

### Prerequisites

-   Python 3.12.X or higher (due to django 6.0.1 requirements)
-   pip (Python package manager)
-   Git
-   A relational database (PostgreSQL recommended for production, SQLite works for development)

### Step 1: Clone the Repository

```bash
git clone https://github.com/lewis1190/ci-hackathon-3-group-1.git
cd ci-hackathon-3-group-1
```

### Step 2: Create a Virtual Environment

Creating a virtual environment keeps project dependencies isolated from your system Python.

### Step 3: Install Dependencies

With your virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Create Environment Configuration

Create an `env.py` file in the project root directory to store sensitive configuration:

Edit `env.py` and add the following configuration (replace placeholders with actual values):

```python
import os

os.environ.setdefault("DEBUG", "True")

# Django secret key - generate a new one for production
SECRET_KEY = 'your-secret-key-here'

# Database configuration (if using PostgreSQL)
# DATABASE_URL = 'postgresql://user:password@localhost:5432/tickit_db'

# Cloudinary configuration (if using cloud storage)
# CLOUDINARY_URL = 'cloudinary://api_key:api_secret@cloud_name'
```

### Step 5: Run the Development Server

Start the local development server:

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

Access the admin panel at: `http://127.0.0.1:8000/admin/` (use your superuser credentials)

---

## Project Structure

-   `tickit/` - Main Django project settings and configuration
-   `home/` - Home application
-   `todos/` - Todos application
-   `templates/` - HTML templates for all applications
-   `static/` - CSS, JavaScript, and image files
-   `requirements.txt` - Python package dependencies
-   `manage.py` - Django management script

## Key Technologies

-   **Django 6.0.1** - Web framework
-   **django-allauth** - Authentication and account management
-   **PostgreSQL** - Production database
-   **Cloudinary** - Cloud media storage
-   **django-summernote** - Rich text editor
-   **crispy-bootstrap5** - Bootstrap form styling
-   **Gunicorn** - WSGI HTTP Server (production)

## Environment Variables

The application uses `env.py` for development configuration. The following can be configured:

-   `SECRET_KEY` - Django secret key (required)
-   `DEBUG` - Set to `'True'` for development mode
-   `DATABASE_URL` - Database connection string (optional, uses SQLite by default)
-   `CLOUDINARY_URL` - Cloudinary cloud storage credentials (optional)
