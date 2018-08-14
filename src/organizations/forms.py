from django import forms

from .models import Organization

class CreateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            'name',
            'address',
            'phone',
            'email',
            'contact_person1',
            'contact_person2',
            'mobile1',
            'mobile2',
            'logo',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of School or College'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address of School or College'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'abc@gmail.com'}),
            'contact_person1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Principal or Co-Ordinatior'}),
            'contact_person2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IT Officer'}),
            'mobile1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile number of principal or Co-Ordinatior'}),
            'mobile2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Moblile number of IT Officer'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }