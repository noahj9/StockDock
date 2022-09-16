# PrintSoftware
## AR print software

Python version 3.10.1: https://www.python.org/downloads/release/python-3101/



### HOW TO START:

1. Clone Repo
2. navigate to subfolder: for me:C:\Users\user1\Documents\Projects\PrintSoftware
3. run activate through scripts: .\Scripts\activate (this activates the virtual environment) (has to be in the project folder)
4. run pip install -r requirements.txt (installs all dependencies)

### Using manage.py to setup and run the server

1. navigate to subfolder
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver (this runs the dev server)

### NOTES FOR ZUNAID
1. Do we want database backups daily?
2. If there are multiple jobs as part of a docket how will this translate to the printed out pdf docket? New pdf docket for each job?
3. 

### CODE TO RUN FOR NOAH: (oin main PC)

cd C:\Users\user1\Documents\Projects\PrintSoftware
.\Scripts\activate
cd webApp_PrintSoftware
python manage.py

START with fresh database:
1. Delete the sqlite database file (often db.sqlite3) in your django project folder (or wherever you placed it)
2. Delete everything except __init__.py file from migration folder in all django apps
3. Make changes in your models (models.py).
4. Run the command python manage.py makemigrations or python3 manage.py makemigrations
5. Then run the command python manage.py migrate.
