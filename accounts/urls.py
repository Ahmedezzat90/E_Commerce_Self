
from django.urls import include, path

from . import views

app_name='E_CommerceSelf'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('logged_out',views.logged_out , name='logged_out'),
    path('profile/', views.profile, name='profile'),  # Define a URL pattern for the 'profile' view
    path('profile/edit',views.profile_edit , name='profile_edit'),

]