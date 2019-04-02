from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.listview, name='list'),
    path('add/', views.createview, name='create'),
    path('<id>/edit/', views.editview, name='edit'),
    path('<id>/delete/', views.deleteview, name='delete'),
    path('branch_list/', views.branch_listview, name='branch_list'),
    path('branch_add/', views.branch_create_view, name='branch_create'),
    path('branch_list/<id>/branch_edit/', views.branch_edit_view, name='branch_edit'),
    path('branch_list/<id>/branch_delete/', views.branch_delete_view, name='branch_delete'),
    path('problem_list/', views.problem_listview, name='problem_list'),
    path('problem_add/', views.problem_create_view, name='problem_create'),
    path('problem_list/<id>/branch_edit/', views.problem_edit_view, name='problem_edit'),
    path('problem_list/<id>/branch_delete/', views.problem_delete_view, name='problem_delete'),
]