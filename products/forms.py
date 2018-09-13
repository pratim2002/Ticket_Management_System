from django import forms

from .models import Product


class CreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }