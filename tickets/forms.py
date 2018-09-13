from django import forms

from .models import Ticket


class CreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'organization_id',
            'ticket_type',
            'product_id',
            'description',
            'completion_date',
            'status',
            'employee_id',
            'attached_file',
        ]
        widgets = {
            'organization_id': forms.Select(attrs={'class': 'form-control'}),
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'completeion_date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'employee_id': forms.Select(attrs={'class': 'form-control'}),
            'attached_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

