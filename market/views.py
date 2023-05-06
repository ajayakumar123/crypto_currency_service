from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from .serializers import UserSerializer

# Create your views here.


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
