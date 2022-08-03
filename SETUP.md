These instructions are for the ubuntu 20.04 operating system.

Install the virtual environment:

`python3 -m venv env`

Activate the virtual environment:

`source env/bin/activate`

Install requirements.txt:

`pip install -r requirements.txt`

Make migrations and migrate with the following commands(manage.py is in the game_store directory):

`python manage.py makemigrations`

`python manage.py migrate`

Load fixtures:

`python manage.py loaddata ../dump.json`

Run the server:

`python manage.py runserver`
