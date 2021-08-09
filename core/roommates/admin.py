from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import User, UserImageGallery, Listing, ListingImageGallery


# Register your models here.
class UserImageInline(admin.TabularInline):
    model = UserImageGallery


class ListingImageInline(admin.TabularInline):
    model = ListingImageGallery


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserImageInline,
    ]

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [
        ListingImageInline,
    ]
    