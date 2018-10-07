from django.urls import reverse

from .base import BaseTestCase


class TestUserRegistration(BaseTestCase):
    
    def test_user_retrieval(self):
        """
        test user logged in retrieved successfully
        """
        self.uri = "/api/user/";
        self.client.login(email="test@test.com", password="test12345")
        self.set_authorization_headers(reverse('login'))
        response = self.client.get(self.uri, format="json")
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("test", str(response.data))
        self.assertIn("test@test.com", str(response.data))
    
    def test_user_retrieval_when_not_logged_in(self):
        """
        test user retrieval when not logged in
        """
        self.uri = "/api/user/";
        self.client.login(email="test@test.com", password="test12345")
        # self.set_authorization_headers(reverse('authentication:login'))
        response = self.client.get(self.uri, format="json")
        self.assertEqual(response.status_code, 403,
                         'Expected Response Code 403, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("Authentication credentials were not provided.",
                      str(response.data))
