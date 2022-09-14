# PrintSoftware
AR print software

Python version 3.10.1: https://www.python.org/downloads/release/python-3101/



HOW TO START:

navigate to subfolder:
for me: C:\Users\user1\Documents\Projects\PrintSoftware
run activate through scripts: .\Scripts\activate (this activates the virtual environment)

navigate to subfolder
use manage.py

python manage.py makemigrations
python manage.py migrate

python manage.py runserver (this runs the dev server)


CODE TO RUN FOR NOAH: (oin main PC)

cd C:\Users\user1\Documents\Projects\PrintSoftware
.\Scripts\activate
cd webApp_PrintSoftware
python manage.py

START with fresh database:
Delete the sqlite database file (often db.sqlite3) in your django project folder (or wherever you placed it)
Delete everything except __init__.py file from migration folder in all django apps
Make changes in your models (models.py).
Run the command python manage.py makemigrations or python3 manage.py makemigrations
Then run the command python manage.py migrate.
