# Gaming_store_API

API za web prodavnicu gaming opreme u Django REST Framework-u

Final project @ developers-lab.me.

Rutiranje unutar API:
- http://127.0.0.1:8000/api/register/ - POST zahtjev sa parametrima username, password, email, first_name, last_name.
- http://127.0.0.1:8000/api/token/ - POST zahtjev sa parametrima username, password. Vrace access i refresh token i informacije o korisniku kao odgovor.
- http://127.0.0.1:8000/api/token/refresh/ - POST zahtjev koji koristi refresh token i na osnovu njega pravi novi access token. 
- http://127.0.0.1:8000/api/inactive/ - GET request koji sadrzi informacije o neaktivnim korisnicima.
- http://127.0.0.1:8000/api/inactive/(id od user-a)/ - GET,PUT i DELETE zahtjevi, PUT zahtjev prihvata is_active kao podatak i mijenja ga u true ili false. Ukoliko se proslijedi drugi parametar vraca se greska u odgovoru. Samo admin moze uspjesno izvrsiti ove zahtjeve.
- http://127.0.0.1:8000/api/category/ - GET i POST zahtjevi za dodavanje i gledanje kategorija. U POST zahtjevu se salju name i image(kao fajl), samo admin ima permisije za POST dok svi ostali mogu da gledaju dostupne kategorije.
- http://127.0.0.1:8000/api/category/(id kategorije)/ - GET zahtjev vrace jednu kategoriju, ukoliko ne postoji trazena kategorija vrace 404 error. Nisu potrebne permisije za ovaj zahtjev.
- http://127.0.0.1:8000/api/manufacturer/ - GET i POST zahtjevi. Parametri za POST je samo name, samo admin moze da dodaje proizvodjace.
- http://127.0.0.1:8000/api/manufacturer/(id od proizvodjaca)/ - GET zahtjev vrace trazenog proizvodjaca.
- http://127.0.0.1:8000/api/component_type/ - GET i POST zahtjevi. Parametar za POST je samo name, samo admin moze da dodaje tipove komponenata.
- http://127.0.0.1:8000/api/manufacturer/(id od proizvodjaca)/ - GET zahtjev vrace trazen tip komponente.
- http://127.0.0.1:8000/api/component/ - GET i POST. Parametri za POST su name, type(id od objekta tipa komponente), manufacturer(od od objekta proizvodjaca)
- http://127.0.0.1:8000/api/component/(id komponente)/ - GET zahtjev vrace podatke o komponenti.
- http://127.0.0.1:8000/api/product/ - GET i POST zahtjevi. POST zahtjev kao podatke prihvata name,description,image,price,manufacturer(id od proizvodjaca),category(id od kategorije), takodje samo admin ima pravo na POST request.
- http://127.0.0.1:8000/api/product/(id od proizvoda)/ - GET zahtjev koji izmedju ostalog vrace i podatke o specifikacijama koje proizvod ima
- http://127.0.0.1:8000/api/specifications/ - GET i POST zahtjev. Na POST-u se salju sledeci podaci product(id od proizvoda), component(id od komponente) i quantity koji ako se ne unese po defaultu je 1. Samo admin korisnik moze da dodaje specifikacije.
- http://127.0.0.1:8000/api/specifications/(id od specifikacije)/ - vrace trazenu specifikaciju
- http://127.0.0.1:8000/api/rating/ - GET i POST zahtjev. U POST zahtjevu se salju sledeci podaci user(id od user-a), product(id od product-a), rating(broj od 1 do 5), i comment.
- http://127.0.0.1:8000/api/rating/(id od recenzije)/ - vrace specificno navedenu recenziju
- http://127.0.0.1.:8000/api/profile/(id od korisnika)/ - PUT zahtjev kojem se salje avatar(slika), i koji postavlja avatar sliku za tog korisnika. PATCH zahtjev kojem se mogu poslati bilo koji podaci osim admin, i password.
- http://127.0.0.1.:8000/api/order/ - GET i POST zahtjev. GET vrace sve order-e od trenutno ulogovanog user-a. POST zahtjeva sledece podatke user(id od user-a), product(id od proizvoda) i quantity. Korisnik mora biti ulogovan za ove zahtjeve
- http://127.0.0.1.:8000/api/order/(id od order-a)/ - DELETE zahtjev brise zahtjevan order. Kada korisnik klikne na "buy" dugme svi orderi trebaju biti obrisani, a balance na korisniku treba biti promijenjen.