import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class MarketsListView(APIView):
    ''' Helpful to get the all the market summeries'''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        response = requests.get("https://api.bittrex.com/v3/markets/summaries")
        if response.status_code == 200:
            return Response(response.json(), status= status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status= response.status_code)


class MarketsDeatilView(APIView):
    '''To get the market detail summery based on symbol'''
    def get(self, request, symbol, fromat=None):
        response = requests.get(f"https://api.bittrex.com/v3/markets/{symbol}/summary")
        if response.status_code == 200:
            return Response(response.json(), status= status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status= response.status_code)
