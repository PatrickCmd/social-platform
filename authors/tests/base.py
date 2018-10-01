from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model


class BaseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = self.setup_user()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="test12345"
        )
        return user
    
    def login_client(self, uri):
        params = {
            "email": "test@test.com",
            "password": "test12345"
        }
        response = self.client.post(uri, params, format="json")
        return response
    
    def set_authorization_headers(self, uri):
        self.token = self.login_client(uri).data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token
        )
