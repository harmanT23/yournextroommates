from django.urls import path
from .views import ListingList, ListingDetail, UserCreate, UserDetail

app_name = 'roommates_api'

urlpatterns = [
    # Get a list of listings or create single listing
    path('listings/', ListingList.as_view(), name='createListings'),
    # Read, update or delete a specific listing
    path('listings/<int:pk>/', ListingDetail.as_view(), name='detailListing'),
    # Create a single user
    path('users/', UserCreate.as_view(), name='createUsers'),
    # Read, update or delete a specific user
    path('users/<int:pk>/', UserDetail.as_view(), name='detailUser'),
    # Create a landing page for API 
]
