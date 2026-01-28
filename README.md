# TickIt - A Task Management Django Application

## Installation & Setup Instructions

Follow these steps to set up and run this Django project on a new machine.

### Prerequisites

-   Python 3.9 or higher
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

## Troubleshooting

TODO
