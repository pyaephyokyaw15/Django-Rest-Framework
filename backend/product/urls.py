from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductCreateAPIVIew.as_view()),
    path('list/', views.ProductListAPIView.as_view()),
    path('list/create/', views.ProductListCreateAPIVIew.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
