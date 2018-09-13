from django import forms
from .models import Employee


class CreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'mobile',
            'email',
            'department',
            'position',
            'picture',
        ]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'first name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'middle name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'mobile number'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'example@zeftware.com'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department'}),
            'position' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'position'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }