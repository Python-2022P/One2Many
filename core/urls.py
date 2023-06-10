from django.contrib import admin
from django.urls import path, include
from ecommerce.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/',include('ecommerce.urls')),
    path("home/<>str:username", HomeView.as_view()),
]
