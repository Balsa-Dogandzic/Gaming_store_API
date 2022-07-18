# Gaming_store_API

API za web prodavnicu gaming opreme u Django REST Framework-u

Final project @ developers-lab.me.

Rutiranje unutar API:
- http://127.0.0.1:8000/api/register/ - POST zahtjev sa parametrima username, password, email, first_name, last_name.
- http://127.0.0.1:8000/api/token/ - POST zahtjev sa parametrima username, password. Vrace access i refresh token i imformacije o korisniku kao odgovor.
- http://127.0.0.1:8000/api/users/ - GET request koji sadrzi informacije o korisnicima. Moguc je pristup samo ako se navede validni access token u autentikaciji
