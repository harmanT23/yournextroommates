from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        
        if email is None:
            raise ValueError(_('User must have email'))
        if extra_fields.get('first_name') is None:
            raise ValueError(_('User must have first name'))
        if extra_fields.get('last_name') is None:
            raise ValueError(_('User must have last name'))
        if extra_fields.get('date_of_birth') is None:
            raise ValueError(_('User must have date of birth'))
        if extra_fields.get('about_me') is None:
            raise ValueError(_('User must have about me'))
        if extra_fields.get('current_city') is None:
            raise ValueError(_('User must have a current city'))
        if extra_fields.get('current_province') is None:
            raise ValueError(_('User must have a current province'))
            
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', 'Super')
        extra_fields.setdefault('last_name', 'User')
        extra_fields.setdefault('date_of_birth', timezone.now().date())
        extra_fields.setdefault('about_me', 'I am super user')
        extra_fields.setdefault('current_city', 'Toronto')
        extra_fields.setdefault('current_province', 'Canada')
        extra_fields.setdefault('is_lister', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        if extra_fields.get('is_lister') is not False:
            raise ValueError(_('Superuser must have is_vendor=False'))

        return self.create_user(email, password, **extra_fields)
        