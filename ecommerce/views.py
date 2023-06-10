from django.http import HttpRequest
from django.views import View
from .models import Company,Product
from django.shortcuts import render


class CompanyView(View):
    def get(self, request: HttpRequest):
        companies = Company.objects.all()

        return render(request, 'company.html', {'companies': companies})
