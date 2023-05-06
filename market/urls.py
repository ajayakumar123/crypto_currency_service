from django.urls import path, include
from market import views

urlpatterns = [
    path('test_view',views.test_view),
]