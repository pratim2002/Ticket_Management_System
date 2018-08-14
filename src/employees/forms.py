from django import forms
from .models import Employee

class CreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'mobile',
            'email',
            'position',
            'picture',
        ]

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'name'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'mobile number'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'example@zeftware.com'}),
            'position' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'position'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }