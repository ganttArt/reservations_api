# Reservations API
API for restaurant table reservation service.  
Includes Django Admin panel & Django REST framework interface for moderators to edit data.
Built with Python3 & Django REST Framework.

## API Endpoints:

- GET - List of all tables  
http://localhost:8000/api/table

- GET - All tables reserved for a given date
http://localhost:8000/api/reservation/by_date/2020-11-27

- POST - Make a reservation  
http://localhost:8000/api/reservation  
body: `{"table": 1, "date":"2020-11-27"}`

## For Moderators to edit data
- Django REST Framework interface  
http://localhost:8000/api/  
- Use Django Admin panel  
http://localhost:8000/admin/
