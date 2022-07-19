# Gaming_store_API

API za web prodavnicu gaming opreme u Django REST Framework-u

Final project @ developers-lab.me.

Rutiranje unutar API:
- http://127.0.0.1:8000/api/register/ - POST zahtjev sa parametrima username, password, email, first_name, last_name.
- http://127.0.0.1:8000/api/token/ - POST zahtjev sa parametrima username, password. Vrace access i refresh token i informacije o korisniku kao odgovor.
- http://127.0.0.1:8000/api/token/refresh/ - POST zahtjev koji koristi refresh token i na osnovu njega pravi novi access token. 
- http://127.0.0.1:8000/api/inactive/ - GET request koji sadrzi informacije o neaktivnim korisnicima.