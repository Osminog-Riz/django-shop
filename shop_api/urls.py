from django.urls import path

from shop_api import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view()),
    path('products/', views.ProductListCreate.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view()),
]
