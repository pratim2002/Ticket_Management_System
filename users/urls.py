from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.user_password_change, name = 'change_password'),
]