from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse
from Products.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer , CartItemSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.


def Cart_Page(request):
    user = request.user
    Carts = Cart.objects.get(user=user)
    Cart_items = CartItem.objects.filter(Carts=Carts)
    context = {'Cart_items': Cart_items}
    return render(request, 'Cart.html', context)

def Add_to_cart(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        Product = Product.objects.get(id=id)
        Cart = Cart.objects.filter(user=user).first()  # Try to get existing cart
        
        if not Cart:
            Cart = Cart(user=user)
            Cart.save()
        Cart_item = CartItem.objects.filter(Carts=Carts, Product=Product).first()
        if not cart_item:
            Cart_item = CartItem(Carts=Carts, Product=Product)
            Cart_item.save()
        else:
            Cart_item.quantity += 1
            Cart_item.save()
        serializer = CartSerializer(Carts)
        if serializer.is_valid():
            serializer.save()
            req_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f'error in add_to_cart => {e}')
        req_status = status.HTTP_404_NOT_FOUND

    return redirect('Home_page')  # Redirect to the home page or wherever you want

def Delete_from_cart(request, id):
    user = request.user
    Product = Product.objects.get(id=id)
    try:
        Cart = Cart.objects.get(user=user)
        Cart_item = CartItem.objects.get(Cart=Cart, Product=Product)
        serializer = CartSerializer(Cart)
        
        req_status = status.HTTP_200_OK
        Cart_item.delete()
        req_status= status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in Delete_from_cart => {e}')
    return redirect('Cart_page')  # Redirect to the home page or wherever you want

def Clear_cart(request):
    user = request.user
    try:
        Cart = Cart.objects.get(user=user)
        Cart.items.all().delete()
        req_status = status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in clear_cart => {e}')
    
    return redirect('Cart_page')  # Redirect to the home page or wherever you want

#--------------------api-------------------------

@api_view(['GET'])
def view_cart(request):
    req_status = status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart, many=True)
        req_status = status.HTTP_200_OK
        return Response(serializer.data)
    except Exception as e:
        print(f'error in all_book_api => {e}')   


@api_view(['POST'])
def Add_to_cart_api(request, product_id):
    req_status = status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.filter(user=user).first()  # Try to get existing cart
        
        if not cart:
            cart = Cart(user=user)
            cart.save()

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        
        if not cart_item:
            cart_item = CartItem(cart=cart, product=product)
            cart_item.save()
        else:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartSerializer(cart)

        if serializer.is_valid():
            serializer.save()
            req_status = status.HTTP_201_CREATED
        
    except Exception as e:
        print(f'error in add_to_cart => {e}')
        req_status = status.HTTP_404_NOT_FOUND

    return Response(serializer.data, status=req_status)

@api_view(['POST'])
def Delete_from_cart_api(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        serializer = CartSerializer(cart)
        
        req_status = status.HTTP_200_OK
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            req_status= status.HTTP_202_ACCEPTED
        else:
            cart_item.delete()
            req_status= status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in Delete_from_cart => {e}')
    return Response(serializer.data,status=req_status)
    

@api_view(['DELETE'])
def Clear_cart_api(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        cart.items.all().delete()
        req_status = status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in clear_cart => {e}')
    
    return Response({"message": "Cart cleared"})






