from django.urls import path
from rest_framework.schemas import get_schema_view
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
    path('listings/', ListingListView.as_view()),
    path('listings/<slug:slug>/', ListingDetailView.as_view()),
    path('users/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('galleries/', GalleryCreateView.as_view()),
    path('galleries/<uuid:gallery_id>/', GalleryDetailView.as_view()),
    path('galleries/<uuid:gallery_id>/<uuid:image_id>/', ImageDetailView.as_view()),
    path('logout/blacklist/', BlackListTokenView.as_view(), name='blacklistToken'),
    path('', get_schema_view(
        title="YourNextRoommates API",
        description="API for creating listings, registering users and viewing galleries",
        version="1.0.0"
    ), name='openapi-schema'),
]
