from django.urls import path
#from .views import PostListing, PostListingList

app_name = 'roommates_api'

urlpatterns = [
    # # Create a single listing
    # path('<int:pk>/', PostListing.as_view(), name='createListing'),
    # # Create a list of listings
    # path('', PostListingList.as_view(), name='createListingList'),
]
