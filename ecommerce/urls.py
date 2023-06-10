from django.urls import path
from .views import CompanyView, ProductView


urlpatterns = [
    path('',CompanyView.as_view()),
    path('products/',ProductView.as_view()),
]