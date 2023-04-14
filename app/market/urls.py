from django.urls import path
from market.views import MarketDataView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", MarketDataView.as_view()),
]
