from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.listview, name = 'list' ),
    path('employees/add/', views.createview, name = 'create'),
    path('<id>/edit', views.editview, name = 'edit'),
    path('<id>/delete', views.deleteview, name = 'delete'),
]