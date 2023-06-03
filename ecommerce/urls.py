from django.urls import path
from .views import *

urlpatterns = [
    
    path("companies",compines),
    path("company/<int:company_id>",get_by_compiny),
    path("companies/<int:company_id>/products",get_by_company_id_all_products),
    path("companies/<int:company_id>/products/<int:id>",get_products_by_id),
    

]

    