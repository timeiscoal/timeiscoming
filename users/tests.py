from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User
from rest_framework import status
# Create your tests here.

class UserRegistrationsAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data= {
            "username" :"testuser",
            "fullname": "테스트",
            "email" : "test@test.com",
            "password":"password",

        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.json() , {
            "message": "가입 완료!!"

        })

    # def test_login(self):
    #     url = reverse("token_obtain_pair")
    #     user_data = {
            
    #         "username" :"testuser",
    #         "fullname": "테스트",
    #         "email" : "test@test.com",
    #         "password":"password",


    #     }
    #     response = self.client.post(url,user_data)
    #     self.assertEqual(response.status_code,200)


    class LoginUserTest(APITestCase):
        def setUp(self):
            self.data = {"username": "john","pasword":"password123"}
            self.user = User.objects.create_user("john", "password123")

        def test_login(self):
            response = self.client.post(reverse("token_obtain_pair"),self.data)
            self.assertEqual(response.status_code, 200)