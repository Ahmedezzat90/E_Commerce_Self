from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cart_Page, name='Cart_page'),
    path('<int:id>/add', views.Add_to_cart, name='Add_to_cart'),
    path('<int:id>/delete', views.Delete_from_cart, name='Delete_from_cart'),
    path('clear', views.Clear_cart, name='Clear_cart'),

    #  _________________________ rest framework ________________________

    path('api', views.view_cart, name='view_cart'),
    path('api/<int:id>/add', views.Add_to_cart_api, name='Add_to_cart_api'),
    path('api/<int:id>/delete', views.Delete_from_cart_api, name='Delete_from_cart_api'),
    path('api/clear', views.Clear_cart_api, name='Clear_cart_api'),


]