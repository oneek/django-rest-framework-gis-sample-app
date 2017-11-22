# Example DRF Gis usage
Sample django app which use [Geographic add-ons for Django REST Framework](https://github.com/djangonauts/django-rest-framework-gis)
This app is a storehouse of information about the services provided by companies at a specific geographic point

###  Setup
1. Clone repo
2. Install required packages with ```pip install -r requirements.txt```
3. install posgresql and postgis extensions
4. Create db, user, activate postgis with psql ```sudo -u postgres psql postgres;```
   ```
   postgres=# create user test_dev with password 'secret';
   postgres=# create database app_db;
   postgres=# grant all privileges on database app_db to test_dev ;
   CREATE DATABASE
   postgres=# \c app_db;
   psql (10.1, server 9.6.6)
   Connected to db app_db
   app_db=# CREATE EXTENSION postgis;
   CREATE EXTENSION
   ```
5. Set db requisites to ```service_api/service_api/settings.py```
6. Create superuser and runserver
   ```
   ./manage.py createsuperuser
   ./manage.py runserver
   ```
### Example usage
For python see ```debug.py```
Example GET uri to get services in ```POINT(5 5)```(need be urlencoded):
```
http://127.0.0.1:8000/servicetypeareaprice/?contains_geom={ "type": "Point", "coordinates": [ 5, 5 ] }
```

### Admin
django admin available at ```/admin``` slug


