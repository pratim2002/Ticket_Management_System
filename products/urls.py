from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_listview, name = 'list' ),
    path('add/', views.product_createview, name = 'create'),
    path('<id>/edit', views.product_editview, name = 'edit'),
    path('<id>/delete', views.product_deleteview, name = 'delete'),
]