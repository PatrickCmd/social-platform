from .base import BaseTestCase


class TestUserLogin(BaseTestCase):
    
    def test_user_logins_successfully(self):
        """
        test user logins successfully
        """
        self.uri = "/api/users/login/";
        params = {
            "email": "test@test.com",
            "password": "test12345"
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("test", str(response.data))
        self.assertIn("token", str(response.data))
    
    def test_user_logins_with_wrong_email(self):
        """
        test user logins with wrong email
        """
        self.uri = "/api/users/login/";
        params = {
            "email": "test1@test.com",
            "password": "test12345"
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("A user with this email and password was not found.",
                      str(response.data))
    
    def test_user_logins_with_wrong_password(self):
        """
        test user logins with wrong password
        """
        self.uri = "/api/users/login/";
        params = {
            "email": "test@test.com",
            "password": "test123456"
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("A user with this email and password was not found.",
                      str(response.data))