from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from market import views

urlpatterns = [
    path('user-registration', views.UserCreate.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('markets', views.MarketsListView.as_view(), name='market_list'),
    path('markets/<str:symbol>', views.MarketsDeatilView.as_view(), name='market_detail')
]