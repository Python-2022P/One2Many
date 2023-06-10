from django.urls import path
from .views import CompanyView,get_company_id,get_product, get_product_id


urlpatterns = [
    path('',CompanyView.as_view()),
    path('<int:id>',get_company_id),
    path("<int:id>/products",get_product),
    path('<int:company_id>/produts/<int:id>',get_product_id)
]