Da bi API funkcionisao potrebno je instalirati virtuelno okruzenje. On se instalira na nacin da se u Gaming_store_API direktorijumu pokrene sledeca komanda:

`python3 -m venv env`

U tom folderu bi se sada trebao nalaziti folder pod imenom "env", zatim trebate da aktivirate virtualno okruzenje sledecom komandom:

Na linux-u: `source env/bin/activate`

Na windows-u: `env\Scripts\activate`

Instalirajte requirements.txt:

`pip install -r requirements.txt`

Napravite, pa izvrsite migracije pomocu manage.py(fajl manage.py se nalazi u game_store direktorijumu):

`python manage.py makemigrations`
`python manage.py migrate` 

Pokrenite server:

`python manage.py runserver`
