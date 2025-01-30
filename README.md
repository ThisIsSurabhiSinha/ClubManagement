# Club Management System

## Project Overview
This is a **Club Management System** developed using Django, designed to manage different clubs within our institute - **Indian Institute of Information Technology Kottayam**. The system includes features such as managing club events, members, and resources.

### Live Project  
The project is live and accessible at: [Club Catalyst](https://clubcatalyst-y67f5eu3.b4a.run/)

---

## Features
- Manage multiple clubs.
- Add, edit, and delete club events.
- Membership management.
- Media handling (e.g., event photos, documents).
- Database support via SQLite.

---

## Folder Structure
- **betalabs**, **Home**, **sportec**, **trendles**, **wildbeats**: These are Django apps that represent various modules of the system, each serving different purposes.
- **db.sqlite3**: The database file storing all application data.
- **manage.py**: Django's command-line utility for administrative tasks like running the server, migrations, etc.
- **media/**: Directory for user-uploaded media such as images or documents.

---

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.x
- Django 3.x
- SQLite (default with Django)

---

## Installation and Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ThisIsSurabhiSinha/ClubManagement/
2 **Navigate to the project directory**:
   ```bash
   cd Club
3.Install dependencies: It is recommended to use a virtual environment.

    ```bash
    pip install -r requirements.txt
4.**Apply migrations**:

    ```bash
    python manage.py migrate
5.**Run the development server**:

    ```bash
    python manage.py runserver
6.**Access the application**:
    Open your browser and navigate to http://127.0.0.1:8000 to view the project.
