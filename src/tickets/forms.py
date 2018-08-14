from django import forms

from .models import Ticket

class CreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'organization_id',
            'ticket_type',
            'description',
            'issue_date',
            'completion_date',
            'status',
        ]
        widgets = {
            'organization_id': forms.Select(attrs={'class': 'form-control'}),
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'issue_date'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'completeion_date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }