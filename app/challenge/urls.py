from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("market/", include("market.urls")),
    path("auth/", include("users.urls")),
    path("admin/", admin.site.urls),
]
