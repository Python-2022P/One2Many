from django.shortcuts import render
from django.http import HttpRequest,JsonResponse,HttpResponse
from json import loads
from .models import Company,Product

# Create your views here.

def to_dict_by_company(data: Company):
    
    return {
        "id": data.pk,
        "name":data.name,
        "website":data.website
    }

def to_dict_product(data: Product):
    
    return {
        "id": data.pk,
        "name": data.name,
        "description": data.description,
        "price": data.price,
        "company":to_dict_by_company(data.company)
        }

def compines(request: HttpRequest):
    if request.method=="GET":
        
        data= Company.objects.all()
        
        return JsonResponse({"results": [ to_dict_by_company(company) for company in data]})
    
    return create_company(request)
        
def get_by_compiny(request: HttpRequest,company_id):
    if request.method=="GET":
        
        data= Company.objects.get(id=company_id)
        
        return JsonResponse({"results": to_dict_by_company(data)})
    
    elif request.method=="PUT":
        return update_companies(request,company_id)
    elif request.method=="DELETE":
        name=Company.objects.get(id=company_id).name
        Company.objects.get(id=company_id).delete()
        return JsonResponse({"status":f'{name} company deleted'})
    
    return JsonResponse({"eror":"other type request"})

def create_company(request: HttpRequest):
    
    data=loads(request.body.decode())
    data=Company.objects.create(name=data["name"],website=data["website"])
    
    return JsonResponse({"result":to_dict_by_company(data)})

def update_companies(request: HttpRequest,company_id):
    
    data=loads(request.body.decode())
    datas=Company.objects.get(id=company_id)
    datas.name=data["name"]
    datas.website=data["website"]
    return JsonResponse({"result":to_dict_by_company(datas)})


def get_by_company_id_all_products(request: HttpRequest,company_id):
    
    if request.method=="GET":
        product=Product.objects.filter(company=company_id)        
        data = {
            "result":[to_dict_product(i) for i in product]
                
        }
        return JsonResponse(data)
    #elif request.method=="POST":
        
def get_products_by_id(request: HttpRequest,company_id,id):
    
    if request.method=="GET":
        product=Product.objects.filter(id=id)        
        data = {
            "result":[to_dict_product(i) for i in product]
                
        }
        return JsonResponse(data)
    elif request.method=="POST":
        data=loads(request.body.decode())
        
        datas=Product.objects.create(name=data["name"],description=data["description"],price=data["price"],company=company_id)
        return to_dict_product(datas)
    elif request.method=="PUT":
        data=loads(request.body.decode())
        update=Product.objects.get(id=data[id])
        update.name=data["name"]
        update.name=data["company_id"]
        return to_dict_product(update)
    elif request.method=="DELETE":
        
        data=Product.objects.get(id=id)
        func=to_dict_product(data)
        data.delete()
        return func
        
        
    
    
    
                
    
    

        
        
        