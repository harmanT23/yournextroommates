from django.contrib import admin

from .models import (
    Listing,
    Gallery,
    GalleryImage
)
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Gallery)
admin.site.register(GalleryImage)
    