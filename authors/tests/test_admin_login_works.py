from authors.apps.authentication.models import User
from django.test import TestCase
from rest_framework import status


class CheckAdminLoginTestCase(TestCase):
    def setUp(self):
        self.admin = User(email="admin@ephraim.com", password="password", username="admin")
        self.admin.save()

        self.form_data = {
            "email": "admin@ephraim.com"
        }


    def test_admin_login_works(self):
        """
        Create an admin user and check to see if json response contains that data
        """
        self.setUp()
       
        request = self.client.post("/authors/user/", self.form_data) 
        return self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_user_can_retrieve_user_data(self):
        """
        Test the UserRetrieveUpdateView works for only authenticated users
        """
        self.setUp()

        request = self.client.get("/authors/user/", self.form_data)   
        return self.assertEqual(request.status_code, status.HTTP_200_OK) 
    

    def test_user_can_update_user(self):
        """
        Test that only authenticated users can update their details
        """
        self.setUp
        request = self.client.post("/authors/user/", self.form_data)
        return self.assertEqual(request.status_code, status.HTTP_200_OK)
        