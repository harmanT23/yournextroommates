# YourNextRoommates (YNR)
YourNextRoommates is a web application intended to connect people looking for roommates. 

Over traditional applications in this domain, YNR goes further and provides users the ability to look for exactly the roommates they'd mesh well with.
Users can filter listings by university, major or profession of the associated poster. Furthermore, users can find the exact listing they'd need in terms of earliest move-in date, lease duration, monthly rent and expected recurring expenses. YNR is meant to make finding your next roommates easy and its also made to list your rental property in a practical and efficient manner. Another unique perspective YNR focuses on is social interaction via user profiles, where users can provide contact details, profile picture, a description of themselves and personal photo gallery.

This project is currently hosted at https://yournextroommates.herokuapp.com/
   > Note: Sometimes it may take a few minutes for the frontend to display
     content. This happens when a new backend instance has to be spun up
     following a period of dormancy. 

## Screenshots 
![Register](https://imgur.com/1wY2qgK.jpeg)
![Homepage](https://imgur.com/kcqVkC9.jpeg)
![Listing_1](https://imgur.com/ohr8KeK.jpeg)
![Listing_2](https://imgur.com/M4Vbhww.jpeg)
![UserProfile](https://imgur.com/8KbmUhW.jpeg)

## Built With
### Stack Used
- [React](https://reactjs.org/) - Framework used to design the frontend UI
- [Django](https://www.djangoproject.com/) - Backend Web Application Framework
- [PostgreSQL](https://www.postgresql.org/) - Databased used to store data
- [Node.js](https://nodejs.org/en/) - JavaScript run-time environment 

### Libraries and Services:
- [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit for building WEB APIs
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Provides a JSON Web Token authentication backend for the Django REST Framework

### Django Project Structure
A Django web application is a self-contained package constructed from a number 
of what Django likes to call 'apps' that each provide a specific utility to the
overall application. 

Regarding the Django apps developed for this project, we have **roommates** and 
**roommates_api** that each provide a specific utility: 
- **roommates** app provides the models for the application along with any 
special helpers functions and Django Signals needed to operate on the models.
- **roommates_api** app utilizes the Django Rest Framework to implement the 
views needed for the endpoints, serializers to convert between JSON and model 
datatypes as well as any services needed to support the endpoints.

## Development
### Prerequisites
To run this application you'll need:
- Python 3.9.7 or higher
- NPM 7.21.0 or higher (update by using command ```npm i -g npm```)
- Node.js 14.17.6 or higher
- [Google Geocoding API key](https://developers.google.com/maps/documentation/geocoding/get-api-key)
    > ### Note
    > The API key can be added to a .env file where the expected API key name is GOOGLE_API_KEY. The .env file should be placed in core/core/ 
- A local installation of [PostgreSQL](https://www.postgresql.org/download/)
   > ### Note
   >
   > If you have brew, install PostgreSQL with the following steps:
   >
   > -  `brew install postgresql` to install PostgreSQL
   > -  `brew services start postgresql` to start the PostgreSQL service 
   (stop it with `brew services stop PostgreSQL`)
- A PostgreSQL database titled ```roommates``` with ```postgres``` as the user. 
**Instructions for setting up the database are as follows on Mac OS**:
   > - ```psql postgres```
   > - ```CREATE ROLE postgres WITH LOGIN;```
   > - ```CREATE DATABASE roommates;```
   > - ```\q```
   > ### Note
   > If you prefer to use a different database name or user then please modify the database settings accordingly in ```core/core/settings.py```.

### Getting Started
In order to run the application locally follow the instructions 
below:

- Begin by cloning the repository 
```git clone https://github.com/harmanT23/yournextroommates.git```

#### Start Django Backend
- Install virtualenv: ```pip install virtualenv```
- Change directory to the project folder: ```cd yournextroommates```
- Create a virtual environment: ```virtualenv venv```
- Activate the virtual environment: ```source venv/bin/activate```
- Install python dependencies: ```pip install -r requirements.txt```
- Change directory to core: ```cd core```
- Make Migrations: ```./manage.py makemigrations```
- Apply DB migrations: ```./manage.py migrate```
- Runserver: ```./manage.py runserver```
#### Start React Frontend
- Change directory to client folder:  ```cd client```
- Install dependencies: ```npm install```
- Start frontend: ```npm start```

## YourNextRoommates API
The application provides an API for authentication, user accounts, listings,
galleries and images.

### Authentication Endpoints
- ```POST /api/token/``` - Takes an email and password of a user then 
returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- ```POST /api/token/refresh/``` - Takes a refresh type JSON web token and  returns an access type JSON web token if the refresh token is valid.
- ```POST /api/token/blacklist/``` - Used to blacklist refresh tokens 
after a user logs out.

### User Endpoints
- ```POST /api/users/``` - Register a new user with email, password, first and last name, date of birth, city, and province.
- ```GET /api/users/me/``` - Get details about the currently authenticated user.
- ```GET /api/users/{uuid}/``` - Get details about a specific user 
- ```PUT/PATCH /api/users/{uuid}/``` - Update a specific user's details
- ```DELETE /api/users/{uuid}/``` - Delete a specific user's details 

### Listing Endpoints
- ```GET /api/listings/``` - Get all the listings in the database, filters
can be applied to make the returned set of listings more relevant (see /api/ more details)
- ```POST /api/listings/``` - Create a new listing requires details such as listing title, room desc, etc.
- ```GET /api/listings/{slug}/``` - Get a specific listing
- ```PUT/PATCH /api/listings/{slug}/``` - Update a specific listing
- ```DELETE /api/listings/{slug}/``` - Delete a specific listing

### Gallery Endpoints
- ```POST /api/galleries/``` - Create a gallery for either an existing user or listing, must specify for which entity gallery is being made via the flag <em>is_listing_or_user_gallery</em>
- ```GET /api/galleries/{gallery_id}/``` - Get all the images (as urls) for a specific gallery
- ```POST /api/galleries/{gallery_id}/``` - Upload one or more images to the specified listing
- ```DELETE /api/galleries/{gallery_id}/``` - Delete gallery and all images within it
- ```GET /api/galleries/{gallery_id}/{image_id}/``` - Get a specific image with in a specified gallery
- ```DELETE /api/galleries/{gallery_id}/{image_id}/``` - Delete a specific image with in a specified gallery

## Contributing
1. [Fork it](https://github.com/harmanT23/yournextroommates/fork)
2. Create your feature branch i.e. ```git checkout -b feature/foo```
3. Commit your changes i.e. ```git commit -am 'Add some foo'```
4. Push to branch i.e. ```git push origin feature/foo```
5. Create a new Pull Request

## Authors
[Harman Tatla](https://github.com/harmanT23) - Project Developer
