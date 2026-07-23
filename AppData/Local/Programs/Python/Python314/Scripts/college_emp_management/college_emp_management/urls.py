from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("dashboard.urls")),   # Home page
    path("admin/", admin.site.urls),
]