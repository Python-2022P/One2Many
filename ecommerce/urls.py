from django.urls import path
from .views import CompanyView,CompanyIdView,ProductView,ProductIdView


urlpatterns = [
    path('',CompanyView.as_view()),
    path('<int:id>',CompanyIdView.as_view()),
    path("<int:id>/products",ProductView.as_view()),
    path('<int:company_id>/produts/<int:id>',ProductIdView.as_view())
]