from django.test import TestCase
from django.contrib.auth import get_user_model
from roommates.models import Listing
from django.utils import timezone
from datetime import timedelta

# Create your tests here.

class TestUser(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='example',
                                        first_name='Example',
                                        last_name='Example',
                                        email='example@example.com',
                                        password='7RppAp!~',
                                        date_of_birth=timezone.now(),
                                        about_me='Example User',
                                        university='University of Example',
                                        university_major='Example Study',
                                        current_city='Example City',
                                        current_province='Example Province',
                                        is_lister=True,
                                        is_seeker=False)
        username = f'{user.username}'
        first_name = f'{user.first_name}'
        last_name = f'{user.last_name}'
        email = f'{user.email}'
        about_me = f'{user.about_me}'
        university = f'{user.university}'
        university_major = f'{user.university_major}'
        current_city = f'{user.current_city}'
        current_province = f'{user.current_province}'
        is_lister = f'{user.is_lister}'
        is_seeker = f'{user.is_seeker}'

        self.assertEqual(username, 'example')
        self.assertEqual(first_name, 'Example')
        self.assertEqual(last_name, 'Example')
        self.assertEqual(email, 'example@example.com')
        self.assertEqual(about_me, 'Example User')
        self.assertEqual(university, 'University of Example')
        self.assertEqual(university_major, 'Example Study')
        self.assertEqual(current_city, 'Example City')
        self.assertEqual(current_province, 'Example Province')
        self.assertEqual(is_lister, 'True')
        self.assertEqual(is_seeker, 'False')


class TestListing(TestCase):
    def test_create_listing(self):
        User = get_user_model()
        user = User.objects.create_user(username='example',
                                        first_name='Example',
                                        last_name='Example',
                                        email='example@example.com',
                                        password='7RppAp!~',
                                        date_of_birth=timezone.now(),
                                        about_me='Example User',
                                        university='University of Example',
                                        university_major='Example Study',
                                        current_city='Example City',
                                        current_province='Example Province',
                                        is_lister='True',
                                        is_seeker='False')

        listing = Listing.objects.create(poster=user,
                                         listing_title = 'Example Lisitng',
                                         room_type='BDR',
                                         room_desc='Example Room',
                                         is_furnished=True,
                                         number_of_residents=3,
                                         rent_per_month=899.00,
                                         extra_expenses_per_month=60.00,
                                         address1='44 Example Dr',
                                         postal_code='R2K4K1',
                                         city='Example City',
                                         province='Ontario',
                                         earliest_move_in_date=\
                                            timezone.now().date())
        
        poster_id = f'{listing.poster.id}'
        listing_title = f'{listing.listing_title}'
        room_type = f'{listing.room_type}'
        room_desc = f'{listing.room_desc}'
        is_furnished = f'{listing.is_furnished}'
        number_of_residents = f'{listing.number_of_residents}'
        rent_per_month = f'{listing.rent_per_month}'
        extra_expenses_per_month = f'{listing.extra_expenses_per_month}'
        address1 = f'{listing.address1}'
        postal_code = f'{listing.postal_code}'
        city = f'{listing.city}'
        province = f'{listing.province}'
        earliest_move_in_date = f'{listing.earliest_move_in_date}'
        listing_expiry_date = f'{listing.listing_expiry_date}'
        
        self.assertEqual(poster_id, f'{user.id}')
        self.assertEqual(listing_title, 'Example Lisitng')
        self.assertEqual(room_type, 'BDR')
        self.assertEqual(room_desc, 'Example Room')
        self.assertEqual(is_furnished, 'True')
        self.assertEqual(number_of_residents, '3')
        self.assertEqual(rent_per_month, '899.0')
        self.assertEqual(extra_expenses_per_month, '60.0')
        self.assertEqual(address1, '44 Example Dr')
        self.assertEqual(postal_code, 'R2K4K1')
        self.assertEqual(city, 'Example City')
        self.assertEqual(province, 'Ontario')
        self.assertEqual(earliest_move_in_date, f'{timezone.now().date()}')
        self.assertEqual(listing_expiry_date, 
                         f'{timezone.now().date() + timedelta(days=30)}')
