from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Manager for creating custom users
    """
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates a regular user in the system.
        """
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
        if extra_fields.get('city') is None:
            raise ValueError(_('User must have a current city'))
        if extra_fields.get('province') is None:
            raise ValueError(_('User must have a current province'))
            
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a super user by setting staff and superuser flags to true.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', 'Super')
        extra_fields.setdefault('last_name', 'User')
        extra_fields.setdefault('date_of_birth', '1994-10-07')
        extra_fields.setdefault('about_me', 'I am super user')
        extra_fields.setdefault('city', 'Toronto')
        extra_fields.setdefault('province', 'Ontario')
        extra_fields.setdefault('is_lister', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        if extra_fields.get('is_lister') is not False:
            raise ValueError(_('Superuser must have is_vendor=False'))
        return self.create_user(email, password, **extra_fields)
        