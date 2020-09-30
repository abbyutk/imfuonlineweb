from django import forms
from django.contrib.auth.models import User
from .models import product,sub_category,deliveryboy

class product_form(forms.ModelForm):
    class Meta:
        model = product
        exclude = ('user','type','key','category','subcategory','brand','expdate')
        widgets = {
            'title': forms.TextInput(attrs={'class':'span11','placeholder':'Titel'}),
            'code': forms.TextInput(attrs={'class':'span11','placeholder':'Code'}),
            'name': forms.TextInput(attrs={'class':'span11','placeholder':'Name'}),
            'capacity': forms.NumberInput(attrs={'class':'span11','placeholder':'Capacity'}),
            'quantity': forms.NumberInput(attrs={'class':'span11','placeholder':'Quantity'}),
            'mrp': forms.NumberInput(attrs={'class':'span11','placeholder':'Normal/Coustomer Price '}),
            'ptr': forms.NumberInput(attrs={'class': 'span11', 'placeholder': 'PTR'}),
            'dptr': forms.NumberInput(attrs={'class': 'span11', 'placeholder': 'Discount on PTR'}),
            'cgst': forms.NumberInput(attrs={'class':'span11','placeholder':'Sgst '}),
            'sgst': forms.NumberInput(attrs={'class': 'span11', 'placeholder': 'Sgst '}),
            'batchno': forms.NumberInput(attrs={'class': 'span11', 'placeholder': 'Batch No '}),
            'buy': forms.NumberInput(attrs={'class':'span11','placeholder':'Buy Product'}),
            'get': forms.NumberInput(attrs={'class':'span11','placeholder':'Get Product Free'}),
            'composition': forms.TextInput(attrs={'class':'span11','placeholder':'Composition / mixture of Drugs'}),
        }

class subcategory_form(forms.ModelForm):
    class Meta:
        model = sub_category
        fields = '__all__'
        widgets= {
            "cat":forms.Select(attrs={'class':'span6'}),
            "name":forms.TextInput(attrs={'class':'span6','placeholder':'Sub Category'}),
        }

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields =('username','email','first_name')
        widgets ={
            "username":forms.TextInput(attrs={'class':'span11','placeholder':'Username'}),
            "email":forms.EmailInput(attrs={"class":'span11','placeholder':'Email'}),
            "first_name":forms.TextInput(attrs={'class':'span11','placeholder':'Name'})
        }

class deliveryboy_form(forms.ModelForm):
    class Meta:
        model = deliveryboy
        fields =('name','email','phone')
        widgets ={
            "name":forms.TextInput(attrs={'class':'span11','placeholder':'Name'}),
            "email":forms.EmailInput(attrs={'class':'span11','placeholder':'Email'}),
            "phone":forms.NumberInput(attrs={'class':'span11','placeholder':'Contect'}),
        }
