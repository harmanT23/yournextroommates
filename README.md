# YourNextRoommates
YourNextRoommates (YNR) is a web application intended to connect people looking for roommates. 
Over traditional applications in this domain, YNR goes further and provides users the ability to look for exactly the roommates they'd mesh well with.
Users can filter listings by university, major or profession of a poster. Furthermore, users can find the exact listing they'd need in terms of earliest move-in
date, lease duration and filter by both monthly rent and recurring expenses. YNR is meant to make both finding your next roommates easy and being able to
list your pad to possible roommates easy and detailed. Another unique perspective YNR introduces is user profiles, where users making a listing or looking for
roommates can provide a profile picture, a description of themselves along with a photo gallery that expresses who they are as a individual.
This way, two parties looking to consider living together get a good idea if they'll mesh well and have similar interests.

## Model Overview
The overall database design of YNR.
<br />
<img src="https://github.com/harmanT23/yournextroommates/blob/main/Documentation_Images/ynr_arrow_not.png" height="500">
<figcaption>Fig.1 - Major models within the design of YNR.</figcaption>

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

Create and activate a virtual environment to install dependencies. i.e.
```
source venv/bin/activate
pip install -r requirements.txt
```

After dependencies installed you can activate the backend
```
cd core
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/


