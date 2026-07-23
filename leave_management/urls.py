from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_list, name='leave_list'),
    path('add/', views.leave_create, name='leave_create'),
    path('delete/<int:pk>/', views.leave_delete, name='leave_delete'),
    path('arrangements/', views.arrangement_list, name='arrangement_list'),
    path('arrangements/add/', views.arrangement_create, name='arrangement_create'),
    path('arrangements/update/<int:pk>/', views.arrangement_update_status, name='arrangement_update_status'),
    path(
    'work-arrangement/update/<int:pk>/<str:status>/',
    views.update_work_arrangement,
    name='update_work_arrangement'
    ),
    path(
        'work-arrangement/',
        views.work_arrangement_list,
        name='work_arrangement_list'
    ),
]
