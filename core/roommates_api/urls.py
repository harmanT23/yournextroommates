from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    ListingListView,
    ListingDetailView, 
    UserCreateView,
    UserDetailView,
    GalleryCreateView,
    GalleryDetailView,
    ImageDetailView, 
    BlackListTokenView
)


app_name = 'roommates_api'

urlpatterns = [
    path(
        'users/', 
        UserCreateView.as_view(), 
        name='user_create'
    ),
    path(
        'users/<int:pk>/', 
        UserDetailView.as_view(), 
        name='user_detail'
    ),
    path(
        'listings/', 
        ListingListView.as_view(), 
        name='listing_list'
    ),
    path(
        'listings/<slug:slug>/', 
        ListingDetailView.as_view(), 
        name='listing_detail'
    ),
    path(
        'galleries/', 
        GalleryCreateView.as_view(), 
        name='gallery_create'
    ),
    path(
        'galleries/<uuid:gallery_id>/', 
        GalleryDetailView.as_view(), 
        name='gallery_detail'
    ),
    path(
        'galleries/<uuid:gallery_id>/<uuid:image_id>/', 
        ImageDetailView.as_view(), 
        name='image_detail'
    ),
    path(
        'token/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path(
        'token/blacklist/', 
        BlackListTokenView.as_view(), 
        name='blacklist_token'
    ),
    path(
        '', 
        get_schema_view(
            title="YourNextRoommates API",
            description="API for creating listings, registering users and viewing galleries",
            version="1.0.0"
        ), 
        name='openapi_schema'
    ),
]
