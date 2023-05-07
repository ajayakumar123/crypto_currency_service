from django.test import TestCase
from django.urls import reverse,resolve
from django.test import SimpleTestCase

from rest_framework.test import APITestCase


# Create your tests here.
class UrlTests(SimpleTestCase):

    def get_urls(self):
        registration_url = reverse('registration')
        self.assertEquals(resolve(registration_url).func.view_class, 'UserCreate')


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('registration')
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            'email': "mani@gmail.com",
            'username': "mani",
            'password': "demo@123",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class UserCreateTestView(TestSetUp):

    def test_user_create_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_create_with_data(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)





