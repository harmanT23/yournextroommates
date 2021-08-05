from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from roommates.models import Listing, UserImage, ListingImage
class UserTests(APITestCase):
    def test_read_user(self):
      url = reverse('roommates_api:detailUser', kwargs={'pk':4})
      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
      url = reverse('roommates_api:createUsers')
      data =  {
                "id": 4,
                "username": "example",
                "email": "example@example.com",
                "first_name": "Example",
                "last_name": "Example",
                "date_of_birth": "2021-08-04",
                "about_me": "Example User",
                "university": "University of Example",
                "university_major": "Example Study",
                "profession": "",
                "home_city": "",
                "home_province": "",
                "current_city": "Example City",
                "current_province": "Example Province",
                "is_lister": True,
                "is_seeker": False,
                "listings": 1
            }

      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ListingTests(APITestCase):
    def test_read_listing(self):
        url = reverse('roommates_api:createListings')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_listing(self):        
        data = {
                  "id": '1',
                  "poster": {
                      "id": '4',
                      "date_of_birth": "2021-08-04",
                      "about_me": "Example User",
                      "university": "University of Example",
                      "university_major": "Example Study",
                      "profession": "",
                      "home_city": "",
                      "home_province": "",
                      "current_city": "Example City",
                      "current_province": "Example Province",
                      "is_lister": 'True',
                      "is_seeker": 'False',
                      "listings": '1'
                  },
                  "listing_title": "Example Listing",
                  "room_type": "BDR",
                  "room_desc": "Small Example Room",
                  "is_furnished": 'True',
                  "number_of_residents": '2',
                  "rent_per_month": "899.00",
                  "extra_expenses_per_month": "60.00",
                  "address1": "44 Example Dr",
                  "address2": "",
                  "postal_code": "R2K4K1",
                  "city": "Toronto",
                  "province": "Ontario",
                  "earliest_move_in_date": "2021-08-01",
                  "listing_expiry_date": "2021-09-04",
                  "listing_visits": '0'
                } 

        url = reverse('roommates_api:createListings')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

