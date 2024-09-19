
Club Management System
Project Overview
This is a Club Management System developed using Django, designed to manage different clubs within our institute- Indian Institute of Information Technology Kottayam. It includes features such as managing club events, members, and resources.
Features
•	Manage multiple clubs.
•	Add, edit, and delete club events.
•	Membership management.
•	Media handling (e.g., event photos, documents).
•	Database support via SQLite.
Folder Structure
•	betalabs, Home, sportec, trendles, wildbeats: These are Django apps that represent various modules of the system, each serving different purposes.
•	db.sqlite3: The database file storing all application data.
•	manage.py: Django's command-line utility for administrative tasks like running the server, migrations, etc.
•	media/: Directory for user-uploaded media such as images or documents.
Prerequisites
Before running this project, make sure you have the following installed:
Python 3.x
Django 3.x
SQLite (default with Django)
•	Installation and Setup
•	Clone the repository:
git clone <repository-url>
•	Navigate to the project directory:
bash
cd Club
•	Install dependencies: You may want to use a virtual environment.
pip install -r requirements.txt
• Apply migrations:
python manage.py migrate
•	Run the development server:
Commands:
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000 to view the project.
•	Usage
Admin Panel: You can access the Django admin panel to manage clubs and members by going to http://127.0.0.1:8000/admin.
Use the club management interfaces to create and manage club-related content.
•	Contributing
Feel free to submit issues or pull requests for improvements.


