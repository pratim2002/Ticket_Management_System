from django import forms

from .models import Organization


class CreateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            'username',
            'name',
            'address',
            'phone',
            'email',
            'mobile',
            'is_active',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'abc@example.com'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile number'}),
            'is_active': forms.Select(attrs={'class': 'form-control'}),
        }