from django.urls import path

from . import views

app_name = 'organizations'
urlpatterns = [
    path('', views.listview, name = 'list'),
    path('add/', views.createview, name = 'create'),
    path('<id>/edit/', views.editview, name = 'edit'),
    path('<id>/delete/', views.deleteview, name='delete'),
    path('<id>/detail/', views.detailview, name = 'detail'),
    path('pdf/', views.pdf_generate_view, name='org_pdf'),
]