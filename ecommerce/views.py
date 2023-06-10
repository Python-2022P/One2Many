from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .models import Company,Product
import json
from django.shortcuts import render



class HomeView(View):
    def get(self, request: HttpRequest, username: str):
        companys=Company.objects.all()
  
        context = {
            'username': username,
            'phones': companys,

            }
        return render(request=request, template_name='index.html', context=context)
