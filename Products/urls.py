from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.Contact, name='Contact'),
    path('allcategory', views.All_category, name='All_category'),
    path('addcategory', views.Add_category, name='Add_category'),
    path('<int:id>/deletecategory', views.Delete_category, name='Delete_category'),
    path('', views.All_product, name='Home_page'),
    path('<int:id>/search', views.All_product_id, name='All_product_id'),
    path('<str:name>/search', views.All_product_name, name='All_product_name'),
    path('<int:id>/delete', views.Delete_product, name='Delete_product'),
    path('add_product/', views.Add_product, name='Add_product'),
    path('edit_product/<int:id>', views.Edit_product, name='Edit_product'),
    
    #  _________________________ rest framework ________________________
    path('api', views.All_product_api, name='All_product_api'),
    path('api/<int:id>/search', views.All_product_id_api, name='All_product_id_api'),
    path('api/<str:name>/search', views.All_product_name_api, name='All_product_name_api'),
    path('api/<int:id>/delete', views.Delete_product_api, name='Delete_product-api'),
    path('api/add_product/', views.Add_product_api, name='Add_product_api'),
    path('api/edit_product/', views.Edit_product_api, name='Edit_product_api'),

]