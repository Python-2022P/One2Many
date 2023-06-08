from django.http import HttpRequest,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .models import Company,Product
import json

def to_company(company:Company) -> dict:
    return {
        'id' : company.pk,
        'name': company.name,
        'website':company.website
    }

def to_product(product:Product) -> dict:
    return {
        'id':product.pk,
        'company_id' : product.company.pk,
        'name' : product.name,
        'price' : product.price
    }

class CompanyView(View):
    def get(self,request:HttpRequest) -> JsonResponse:
        companies = Company.objects.all()
        result = [to_company(company) for company in companies]

        return JsonResponse(result,safe=False)
    def post(self,request:HttpRequest) -> JsonResponse:
        data_json = request.body.decode()
        data = json.loads(data_json)
        
        if not data.get('name'):
            return JsonResponse({'status':"name yo'q"})
        elif not data.get('website'):
            return JsonResponse({'status':'website yo\'q'})
        
        company = Company.objects.create(
            name = data['name'],
            website = data['website']
        )

        company.save()

        return JsonResponse(to_company(company))


class CompanyIdView(View):
    def get(self,request:HttpRequest,id) -> JsonResponse:
        company = Company.objects.get(id = id)
        return JsonResponse(to_company(company))
    
    def put(self,request:HttpRequest,id) -> JsonResponse:
        try:
            company = Company.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            company.name = data['name']
        if data.get('website'):
            company.website = data['website']
       

        company.save()

        return JsonResponse(to_company(company))
    
    def delete(self,request:HttpRequest,id) -> JsonResponse:
        try:
            company = Company.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        company.delete()

        return JsonResponse({'status': 'ok'})
    
class ProductView(View):
    def get(self,request:HttpRequest,id) -> JsonResponse:
        try:
            company = Company.objects.get(id = id)
            products = Product.objects.filter(company = company)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        results = [to_product(product) for product in products]
        return JsonResponse(results,safe=False)
    
    def post(self,request:HttpRequest,id) -> JsonResponse:
        data_json = request.body.decode()
        data = json.loads(data_json)

        company = Company.objects.get(id = id)

        product = Product.objects.create(
            user_id = company,
            name = data['name'],
            price = data['price']
        )

        product.save()

        return JsonResponse(to_product(product))
    
class ProductIdView(View):
    

    def get(self,request:HttpRequest,company_id,id) -> JsonResponse:
        try:
            company = Company.objects.get(id = company_id)
            product = Product.objects.get(company=company,id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        return JsonResponse(to_product(product))

    def put(self,request:HttpRequest,company_id,id) -> JsonResponse:
        try:
            company = Company.objects.get(id = company_id)
            product = Product.objects.get(company=company,id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            product.name = data['name']
        if data.get('price'):
            product.price = data['price']

        product.save()

        return JsonResponse(to_product(product))

    def delete(self,request:HttpRequest,company_id,id) -> JsonResponse:
        try:
            company = Company.objects.get(id = company_id)
            product = Product.objects.get(company=company,id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        product.delete()

        return JsonResponse({'status': 'ok'})

