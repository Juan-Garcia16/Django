from django.urls import path
from products.views import ProductDetailView

urlpatterns = [
    path('<pk>/', ProductDetailView.as_view(), name='product'),
]