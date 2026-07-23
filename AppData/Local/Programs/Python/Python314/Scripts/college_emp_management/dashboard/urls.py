from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("reports/", views.reports, name="reports"),

path("download-pdf/", views.download_pdf, name="download_pdf"),
path("download-excel/", views.download_excel, name="download_excel"),
    path("logout/", views.logout_view, name="logout"),
]