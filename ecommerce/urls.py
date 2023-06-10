from django.urls import path
from .views import (
    getall_create_company,
    get_id_update_com_delete_id,
    products_create_get_all,
    product_get_put_del,
)
                     

urlpatterns = [
    path('',getall_create_company),
    path('<int:id>',get_id_update_com_delete_id),
    path('<int:id>/product',products_create_get_all),
    path('<int:id>/product/<int:pro_id>',product_get_put_del)
]