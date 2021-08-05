from django.contrib import admin
from .models import User, UserImage, Listing, ListingImage

# Register your models here.
class UserImageInline(admin.TabularInline):
    model = UserImage


class ListingImageInline(admin.TabularInline):
    model = ListingImage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserImageInline,
    ]

@admin.register(Listing)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        ListingImageInline,
    ]
    