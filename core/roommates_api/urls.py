from django.urls import path, include
from .views import ListingViewset, UserViewset,\
    BlackListTokenView
from rest_framework.routers import DefaultRouter

app_name = 'roommates_api'
router = DefaultRouter()
router.register('listings', ListingViewset, basename='listings')
router.register('users', UserViewset, basename='users')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('logout/blacklist/', BlackListTokenView.as_view(), name='blacklistToken'),
]
     