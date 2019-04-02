from django import forms

from .models import Ticket, Branch, ProblemDomain


class CreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'client_id',
            'contact',
            'branch_id',
            'problem_domain_id',
            'status',
            'remarks',
            'ticket',
            'source',
            'employee_id',
        ]
        widgets = {
            'client_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'client_id'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'contact number'}),
            'branch_id': forms.Select(attrs={'class': 'form-control'}),
            'problem_domain_id': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'ticket': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ticket number'}),
            'source': forms.Select(attrs={'class': 'form-control'}),
            'employee_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateForm, self). __init__(*args, **kwargs)
        self.fields['employee_id'].required = True


class CreateBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'branch name'}),
        }


class CreateProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemDomain
        fields = [
            'problem',
        ]
        widgets = {
            'problem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'problem'}),
        }

