from django import forms
from .models import Category,Product

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name",
            "description",
            "price",
            "brand",
            "image",
            "stock",
            "createAt",
            "availabe",
            "category",
            "user")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            #'ratings': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'createAt': forms.DateTimeInput(attrs={'class': 'form-control' ,'type': 'date'}),
            'availabe': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }