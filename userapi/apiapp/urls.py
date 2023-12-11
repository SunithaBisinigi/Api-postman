# user_registration/urls.py
from django.urls import path
from .views import register_user, warehouse_detail, warehouse_list

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('warehouselist/', warehouse_list, name='warehouse_list'),
    path('warehouse/<int:pk>/', warehouse_detail, name='warehouse_detail'),
    path('warehouse/<int:pk>/delete/', warehouse_detail, name='warehouse_delete'),
]
