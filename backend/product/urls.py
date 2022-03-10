from django.urls import path

from . import views

urlpatterns = [
    # api/products/
    path('', views.ProductCreateAPIVIew.as_view()),
    # path('', views.product_alt_view),
    path('list/', views.ProductListAPIView.as_view()),
    # path('list/', views.ProductMixinView.as_view()),
    path('list/create/', views.ProductListCreateAPIVIew.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    # path('<int:pk>/', views.product_alt_view),
    # path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
]
