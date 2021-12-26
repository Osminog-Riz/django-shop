from django.urls import path
from products import views

urlpatterns = [
    path('', views.index),

    path('categories/', views.categories_list),
    path('categories/<int:pk>/', views.product_list),
    path('products/<int:pk>/', views.product_info),
]
