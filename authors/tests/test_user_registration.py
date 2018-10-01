from .base import BaseTestCase


class TestUserRegistration(BaseTestCase):
    
    def test_user_registers_successfully(self):
        """
        test user registers successfully
        """
        self.uri = "/api/users/";
        params = {
            "username": "test1",
            "email": "test1@test.com",
            "password": "test12345"
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("test1", str(response.data))
        self.assertIn("token", str(response.data))
    
    def test_already_existing_user(self):
        """
        test user registers already exists
        """
        self.uri = "/api/users/";
        params = {
            "username": "test",
            "email": "test@test.com",
            "password": "test12345"
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("user with this email already exists.",
                      str(response.data))
        self.assertIn("user with this username already exists.",
                      str(response.data))
    
    def test_user_registers_with_empty_fields(self):
        """
        test user registers with empty json fields
        """
        self.uri = "/api/users/";
        params = {
            
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
        self.assertIn("This field is required.",
                      str(response.data))
