from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from .forms import Categoryform, Productform

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import Category_serializer, Product_serializer
# Create your views here.

def Contact(request):
    return render(request,'Contact.html')


def All_category(request):
    Categorys = Category.objects.all()
    Context={ 
        'Categorys':Categorys, 
        'Title':'All Category',
    }
    return render(request,'All_category.html',Context)

def Add_category(request):
    Category_form = Categoryform()
    context={}
    try:
        if request.method == 'POST':
            Category_form = Categoryform(request.POST) 
            if Category_form.is_valid():
                Category_form.save()
                return redirect('All_category')
            else:
                Category_form = Categoryform()
        context = {
            'Category_form':Category_form ,
            'Title':'Add Category',
        }
    except Exception as e:
        print(f'error in Add_category => {e}')
    return render(request,'Add_category.html',context)

def Delete_category(request,id):
    try:
        Categorys = get_object_or_404(Category,id=id)
        Categorys.delete()
    except Exception as e:
        print(f'error in Delete_Category => {e}')
    return redirect('All_category')

#------------------product----------------------

def All_product(request):
    Products = Product.objects.all()
    context={ 'Products':Products }
    return render(request,'Home_Page.html',context)

def All_product_name(request,name):
    Products = Product.objects.filter(name=name)
    context={ 'Products':Products }
    return render(request,'Product_details.html',context)

def All_product_id(request,id):
    Products = Product.objects.get(id=id)
    context={ 'Products':Products }
    return render(request,'Product_details.html',context)

def Add_product(request):
    Product_form = Productform()
    context={}
    try:
        if request.method == 'POST':
            Product_form = Productform(request.POST,request.FILES)
            if Product_form.is_valid():
                Product_form.save()
                return redirect('Home_page')
            else:
                Product_form = Productform()
        context = {
            'Product_form':Product_form ,
            'Title':'Add Product',
        }
    except Exception as e:
        print(f'error in Add_product => {e}')
    return render(request,'Add_product.html',context)

def Edit_product(request,id):
    Product_form = Productform()
    context={}
    try:
        if request.method == 'POST':
            products = get_object_or_404(Product,id=id)
            Product_form = Productform(request.POST,request.FILES,instance=products)
            if Product_form.is_valid():
                Product_form.save()
                return redirect('Home_page')
            else:
                Product_form = Productform(instance=products)
        context = {
            'Product_form':Product_form ,
            'Title':'Edit Product',
        }
    except Exception as e:
        print(f'error in Edit_product => {e}')
    return render(request,'Add_product.html',context)

def Delete_product(request,id):
    try:
        products = get_object_or_404(Product,id=id)
        products.delete()
    except Exception as e:
        print(f'error in Delete_product => {e}')
    return redirect('Home_page')

#--------------------api-------------------------
@api_view(['GET'])
def All_product_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = Product.objects.all()
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_api => {e}')
    return Response(data=data, status=req_status)

#--------
@api_view(['GET'])
def All_product_name_api(request,name):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = Product.objects.filter(name__icontains=name)
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_name_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['GET'])
def All_product_id_api(request,id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(Product,id=id)
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_id_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['POST'])
def Add_product_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data={}
    try:
        New_product = Product_serializer(data=request.data)
        if New_product.is_valid():
            New_product.save()
            data['New_product'] = New_product.data
            req_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f'error in New_product_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['PUT'])
def Edit_product_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(Product, id=id)
        x = Product_serializer(instance=products, data=request.data, partial=True)
        if x.is_valid():
            x.save()
            req_status = status.HTTP_200_OK
            data['products'] = x.data
    except Exception as e:
        print(f'error in Edit_product_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['DELETE'])
def Delete_product_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(book, id=id)
        product_serializer = Product_serializer(instance=products).data
        products.delete()
        req_status = status.HTTP_204_NO_CONTENT
        data['products'] = product_serializer
    except Exception as e:
        print(f'error in Delete_product_api => {e}')
    return Response(data=data, status=req_status)
