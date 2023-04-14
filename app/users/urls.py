from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import LoginView, LogoutView, SignUpView

app_name = "users"

urlpatterns = [
    path("accounts/sign-up", SignUpView.as_view(), name="sign_up"),
    path("accounts/login", LoginView.as_view(), name="login"),
    path("accounts/logout", LogoutView.as_view(), name="logout"),
    path(
        "accounts/token-refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
