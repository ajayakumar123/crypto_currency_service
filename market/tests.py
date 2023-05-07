
from django.contrib.auth.models import User
from django.urls import reverse
from market import views
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory


class TestUserCreate(APITestCase):

    def test_create_account_without_data(self):

        url = reverse('registration')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_account(self):
        """
        Ensure we can create a new account.
        """
        url = reverse('registration')
        data = {'email': 'deelip@gmail.com',
                'username': 'deelip',
                'password': 'demo@123'
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'deelip')


user = User.objects.get(username='hradmin')


class TestMarkets(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MarketsListView.as_view()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_list_markets_no_user(self):
        request = self.factory.get('/market/markets')
        force_authenticate(request, user=None)
        response = self.view(request)
        self.assertEqual(response.status_code, 401)

    def test_list_markets(self):
        request = self.factory.get('/market/markets')
        force_authenticate(request, user=user)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestMarketDetailView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MarketsDeatilView.as_view()
        self.symbol = '1ECO-USDT'
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_list_markets_no_user(self):
        request = self.factory.get(f'/market/markets/{self.symbol}')
        force_authenticate(request, user=None)
        response = self.view(request, self.symbol)
        self.assertEqual(response.status_code, 401)

    def test_list_markets(self):
        request = self.factory.get('/market/markets/{self.symbol}')
        force_authenticate(request, user=user)
        response = self.view(request, self.symbol)
        self.assertEqual(response.status_code, 200)





