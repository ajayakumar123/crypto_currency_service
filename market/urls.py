from django.urls import path, include
from market import views

urlpatterns = [
    path('user-registration', views.UserCreate.as_view(), name='registration'),
]