from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Company, Product
import json
from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self, request: HttpRequest, username: str):
        companys=Company.objects.all()
        for i in companys:
            products=Product.objects.filter(company=i)
            context = {
                'username': username,
                'phone': i,
                'products':products
            }
        return render(request=request, template_name='index.html', context=context)
def to_com(company)->dict:
    return {
        'id':company.pk,
        "name":company.name,
        "website":company.website
    }
def to_pro(product:Product):
    return {
        'id':product.pk,
        'name':product.name,
        'description':product.description,
        'price':product.price,
        'company':to_com(product.company)
    }
def getall_create_company(request:HttpRequest) ->JsonResponse:
    if request.method=='GET':

        companys=Company.objects.all()

        result= [to_com(i) for i in companys]

        return JsonResponse(result,safe=False)
    elif request.method=='Post':
        data_json = request.body.decode()
        data = json.loads(data_json)
        
        if not data.get('name'):
            return JsonResponse({'status':"name yo'q"})
        elif not data.get('website'):
            return JsonResponse({'status':'website yoq'})
        
        company = Company.objects.create(
            name = data['name'],
            website = data['website'],     
        )

        company.save()

        return JsonResponse(to_com(Company))
    
    
def get_id_update_com_delete_id(request:HttpRequest,id) -> JsonResponse:
    if request.method=='GET':
        company=Company.objects.get(id=id)
        return JsonResponse(to_com(company))
    elif request.method=='PUT':
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

        return JsonResponse(to_com(company))
    elif request.method == "DELETE":
        try:
            phone = Company.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        phone.delete()
        
        return JsonResponse({'status': 'ok'})
#//////////////////////////////////Many////////////////
def products_create_get_all(request:HttpRequest,id) -> JsonResponse:
    try:
        company = Company.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'object does not exist!'})
    if request.method=='GET':
        products=Product.objects.filter(company=company)
        result=[to_pro(product) for product in products]
        return JsonResponse(result, safe=False)
    if request.method=='POST':
        data_json = request.body.decode()
        data = json.loads(data_json)
        
        if not data.get('name'):
            return JsonResponse({'status':"name yo'q"})
        elif not data.get('price'):
            return JsonResponse({"status":"price yo'q"})
        elif not data.get('description'):
            return JsonResponse({"status":"description yo'q"})
        
        product = Product.objects.create(
            name = data['name'],
            price = data['price'],
            description=data['description'],
            company=company
        )
        product.save()
        return JsonResponse(to_pro(product))
def product_get_put_del(request:HttpRequest,company_id, product_id) -> JsonResponse:
    try:
        company = Company.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'object does not exist!'})
    if request.method=='GET':
        product=Product.objects.filter(company=company).get(id=product_id)
        return JsonResponse(to_pro(product))
    elif request.method=='PUT':
        data_json = request.body.decode()
        data = json.loads(data_json)

        try:
            product = Product.objects.get( id= company_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        if data.get('name'):
            product.name=data['name']
        if data.get('price'):
            product.price=data['price']
        if data.get('description'):
            product.description=data['description']

        product.save()
        return JsonResponse(to_pro(product))
    elif request.method=='DELETE':
        try:
            product = Product.objects.get( id=product_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        product.delete()
        return JsonResponse({'satasus':'ok'})