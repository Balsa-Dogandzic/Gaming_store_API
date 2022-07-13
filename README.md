# Gaming_store_API

Da bi API funkcionisao potrebno je instalirati virtuelno okruzenje. On se instalira na nacin da se u Gaming_store_API direktorijumu pokrene sledeca komanda:

python3 -m venv env

U tom folderu bi se sada trebao nalaziti folder pod imenom "env", zatim trebate da aktivirate virtualno okruzenje sledecom komandom:

Na linux-u:
source env/bin/activate
Na windows-u:
env\Scripts\activate

Izvrsite migracije pomocu manage.py(fajl manage.py se nalazi u game_store direktorijumu):

python manage.py migrate 

Pokrenite server:

python manage.py runserver

Rutiranje unutar API:
- http://127.0.0.1:8000/api/register/ - POST zahtjev sa parametrima username, password, email, first_name, last_name.
- http://127.0.0.1:8000/api/token/ - POST zahtjev sa parametrima username, password. Vrace access i refresh token kao odgovor.
- http://127.0.0.1:8000/api/profile/ - POST zahtjev sa parametrima username, password. Vrace sve informacije o korisniku
- http://127.0.0.1:8000/api/users/ - GET request koji sadrzi informacije o korisnicima. Moguc je pristup samo ako se navede validni access token u autentikaciji
