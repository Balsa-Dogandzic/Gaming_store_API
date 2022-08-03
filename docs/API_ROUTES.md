Endpoint urls of the API:
- http://127.0.0.1:8000/api/register/ - POST request takes username, password, email, first_name, last_name as parameters in the body of the request.
- http://127.0.0.1:8000/api/token/ - POST request takes username and password parameters in the request body. Returns access and refresh tokens and data about the user in the response.
- http://127.0.0.1:8000/api/token/refresh/ - POST request sends refresh token in the body of the request. Returns new valid access token. 
- http://127.0.0.1:8000/api/inactive/ - GET request returns inactive users data.
- http://127.0.0.1:8000/api/inactive/(user_id)/ - GET,PUT and DELETE request, PUT request sends is_active parameter of the user which is true or false. DELETE request deletes the inactive user. Only the admin user has permission for these requests.
- http://127.0.0.1:8000/api/category/ - GET and POST requests for reading and creating product categories. POST request sends name and image(file) in the request body, only admin can add categories, but every user can view the categories.
- http://127.0.0.1:8000/api/category/(category_id)/ - GET request returns data about requested category.
- http://127.0.0.1:8000/api/manufacturer/ - GET and POST requests. POST request sends name in the request body, and only the admin user can add new manufacturers.
- http://127.0.0.1:8000/api/manufacturer/(manufacturer_id)/ - GET request returns the requested manufacturer.
- http://127.0.0.1:8000/api/component_type/ - GET and POST requests. POST request only takes the name in the request body, and only the admin user can add new component types.
- http://127.0.0.1:8000/api/component_type/(component_type_id)/ - GET request returns the requested component type.
- http://127.0.0.1:8000/api/component/ - GET and POST requests. POST sends the following attributes name, type(id of the component type), manufacturer(manufacturer id).
- http://127.0.0.1:8000/api/component/(component_id)/ - GET request returns the requested component.
- http://127.0.0.1:8000/api/product/ - GET and POST requests. POST request sends the following attributes name, description, image(file), price, manufacturer(manufacturer_id), category(category_id), only the admin user has permission for POST request.
- http://127.0.0.1:8000/api/product/(product_id)/ - GET, PUT and DELETE request. GET returns the specified product with his specifications, PUT request updates every attribute that is sent in the request body. DELETE request deletes the specified product. Only the admin user can update and delete products.
- http://127.0.0.1:8000/api/specifications/ - GET and POST request. POST request sends the following attributes product(product_id), component(component_id) and quantity which is 1 by default, only the admin user has permission for POST request.
- http://127.0.0.1:8000/api/specifications/(specification_id)/ - GET request returns the requested specification.
- http://127.0.0.1:8000/api/rating/ - GET and POST request. POST sends the following attributes product(product_id), rating(integer in range from 1 to 5), and the comment. User id is gained from the access token. Only authenticated users can create a rating, but everyone can read them.
- http://127.0.0.1:8000/api/rating/(rating_id)/ - GET request returns the requested rating.
- http://127.0.0.1:8000/api/profile/ - GET returns the authenticated user.
- http://127.0.0.1:8000/api/profile/(user_id)/ - GET request returns authenticated user data. PUT sends avatar attribute in the request body and changes it, avatar is a profile picture. PATCH request updates every attribute except admin,password and balance.
- http://127.0.0.1:8000/api/order/ - GET and POST request. GET request returns every order of the authenticated user. POST sends the following attributes product(product_id) and quantity. User id is gained from the access token. Only the authenticated user has permissions for these requests.
- http://127.0.0.1:8000/api/order/(order_id)/ - DELETE request deletes the specified order.
- http://127.0.0.1:8000/api/payment/(user_id)/ - PUT request changes the balance attribute of the user. The balance in the request body must be lower or equal to the amount the user had before, and the balance in the request must be higher or equal than 0. Only the authenticated user has the permission for this request.

Filters:

- Products can be filtered by category_name, and manufacturer_name that are requested in the url parameters as category and manufacturer.
- Ratings can be filtered by product_name that is requested in the url parameter as product.