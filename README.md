# Movie rest api

## Features
With this API;
- You can create, view, update, and delete a movie, login with a user and register a new user
## Technology stack
Tools used during the development of this API are;
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) - this is a database server
## Requirements
- Use Python 3.x.x+
- Use Django 2.x.x+

## Initial Configuration
- Use the command pip install -r requirementes.txt to install django an djangorestframework library
- Download de postgreSQL installer and install postgreSql, configure the user and password to connecte the api to database.
- create or clone the repository and configure de environment to run the aplication, use the command virtualenv env
- then use cd env/Sripts, and execute activate
- Run the command python manage.py createsuperuser, follow the instructions and write de name, password and email


## Steps

- Configure the archive settings.py in the section DATABASES to change the parameters for your database configuration like in next image.

![database](https://user-images.githubusercontent.com/22681704/56395993-7e4ddf00-6202-11e9-926d-abefa9602f4e.PNG)

## Api url


### Register users
To register a user is necessary create a superuser and login with this user. login using the route http://localhost:8000/api/login/?next=/api/createusers/ and enter the super user and password
then we can create any user for the application like in the image

![createuser](https://user-images.githubusercontent.com/22681704/56398542-b4915b80-620e-11e9-88db-577cf16ebe5f.PNG)

if we select the radio button is_superuser and is_staff, the new user created can login in the console admin

### Login users

use the next url http://localhost:8000/api/login/?next=/api/movies/ and login with user register

### Get a movie list

use the route http://localhost:8000/api/movies/ to get the list of movie in database like in the image

![listmovie](https://user-images.githubusercontent.com/22681704/56398690-7cd6e380-620f-11e9-9228-1757a20111c1.PNG)


### Create a new movie

in the same route http://localhost:8000/api/movies/ on the end of the page we can find the form to create a new movie like in the image

![newmovie](https://user-images.githubusercontent.com/22681704/56398716-ad1e8200-620f-11e9-83b5-ed9ce741fdff.PNG)


### Get a movie

use the route http://localhost:8000/api/movies/2/ when the number in the end of the route is the ID of the register in database.

![getonemovie](https://user-images.githubusercontent.com/22681704/56398783-17372700-6210-11e9-96c8-5edbe54f62a9.PNG)

### Update a movie

use the route http://localhost:8000/api/movies/2/ and in the end of page we can find the form to update the movie

![updatemovie](https://user-images.githubusercontent.com/22681704/56398846-7f860880-6210-11e9-84c9-ec0678b62f5d.PNG)

in this form we can update each textfield and to update select the put botton

### Delete a movie

in the same route we can use the bottom Delete like in the image

![delete](https://user-images.githubusercontent.com/22681704/56398939-e0addc00-6210-11e9-9971-d18214c8ac5a.PNG)
