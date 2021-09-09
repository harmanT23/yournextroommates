# YourNextRoommates
YourNextRoommates (YNR) is a web application intended to connect people looking for roommates. 
Over traditional applications in this domain, YNR goes further and provides users the ability to look for exactly the roommates they'd mesh well with.
Users can filter listings by university, major or profession of a poster. Furthermore, users can find the exact listing they'd need in terms of earliest move-in
date, lease duration and filter by both monthly rent and recurring expenses. YNR is meant to make both finding your next roommates easy and being able to
list your pad to possible roommates easy and detailed. Another unique perspective YNR introduces is user profiles, where users making a listing or looking for
roommates can provide a profile picture, a description of themselves along with a photo gallery that expresses who they are as a individual.
This way, two parties looking to consider living together get a good idea if they'll mesh well and have similar interests.

## Current Status
As of now the back-end has been completed and is usable. I will be working on getting the front-end finished as time permits. 

## Model Overview
<img src="https://github.com/harmanT23/yournextroommates/blob/main/Documentation_Images/ynr_arrow_not.png" height="500">
<figcaption>Database models invovled in YNR.</figcaption>

## Built With
- [React](https://reactjs.org/) - Framework for developing front-end UI
- [Django](https://www.djangoproject.com/) - Back-end web application framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework for developing Web APIs
- [PostgreSQL](https://www.postgresql.org/) - Relational database used to store listings/users and image urls
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/) - Framework for determining testing coverage

## Setup

### Django Backend

Clone Repository
```
git clone https://github.com/harmanT23/yournextroommates.git
cd yournextroommates
cd core
```

Create and activate a python virtual environment to install dependencies. i.e.
```
source venv/bin/activate
pip install -r requirements.txt
```

After dependencies installed you can activate the backend
```
cd core
python manage.py runserver
```

#### Optional
YNR uses the Google Geocoding API for verifying the address posted in a listing. In order to have this portion work, you will need
to acquire an [API key](https://developers.google.com/maps/documentation/geocoding/get-api-key) and assign that to ```GOOGLE_API_KEY``` within the project settings located at ```.../yournextroommates/core/core/settings.py```

Navigate to http://127.0.0.1:8000/

## Acessing the API
YourNextRoommates provides an extensive API for performing a number of operations ranging from the creation of users, listings, galleries and even the blacklisting of authentication tokens after a user is logged out.

A complete API schema is provided in the following links that offers details about parameters, filters and more:
- OpenAPI Schema - http://127.0.0.1:8000/docs/
- CoreAPI Schema - http://127.0.0.1:8000/api/

### Authentication Endpoints
- ```POST /api-auth/login``` - sign-in using username + password to an existing account
- ```GET /api-auth/logout``` - sign-out of the currently authenticated user
- ```POST /api/token/``` - Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- ```POST /api/token/refresh/``` - Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
- ```POST /api/logout/blacklist/``` - Used to blacklist refresh tokens after a user logs out.

### User Endpoints
- ```POST /api/users/``` - Register a new user with username, password, first and last name, date of birth, city, province and a short 'about me' description.
- ```GET /api/users/{id}/``` - Get details about a specific user
- ```PUT/PATCH /api/users/{id}/``` - Update a specific user's details
- ```DELETE /api/users/{id}/``` - Delete a specific user's details 

### Listing Endpoints
- ```GET /api/listings/``` - Get a list of listings, can be made more relevant by specifying filters (see API Schema mentioned above)
- ```POST /api/listings/``` - Create a new listing linked to the currently authenticated user, required details such as listing title, room desc, etc.
- ```GET /api/listings/{slug}/``` - Get a specific listing
- ```PUT/PATCH /api/listings/{slug}/``` - Update a specific listing
- ```DELETE /api/listings/{slug}/``` - Delete a specific listing

### Gallery Endpoints
- ```POST /api/galleries/``` - Create a gallery for either an existing user or listing, must specify for which entity gallery is being made via <em>is_listing_or_user_gallery flag</em>
- ```GET /api/galleries/{gallery_id}/``` - Get a list of image URLS for a specific gallery
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
[Harman Tatla](https://www.linkedin.com/in/harmantatla/) <br />
MS Computer Science, University of Illinois @ Urbana-Champaign  <br />
