from django.urls import path, include
from .views import ListingView, UserView, BlackListTokenView
from rest_framework.routers import DefaultRouter

app_name = 'roommates_api'
router = DefaultRouter()
router.register('listings', ListingView, basename='listings')
router.register('users', UserView, basename='users')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('logout/blacklist/', BlackListTokenView.as_view(), name='blacklistToken'),
]
     