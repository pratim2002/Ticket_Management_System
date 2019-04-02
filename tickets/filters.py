import django_filters
from model_utils import Choices

from tickets.models import Ticket, Branch, ProblemDomain
from django import forms


class TicketFilter(django_filters.FilterSet):
    STATUS = Choices(
        'Open',
        'Close',
        'Pending',
    )
    SOURCE = Choices(
        'Call_in',
        'Call_out',
        'CUG',
        'Viber',
        'Skype',
        'Message',
    )

    username = django_filters.CharFilter(
        field_name='client_id',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )

    branch = django_filters.ModelChoiceFilter(
        label='Client',
        field_name='branch_id',
        queryset=Branch.objects.all(),
        empty_label='Select Branch',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    problem_domain = django_filters.ModelChoiceFilter(
        label='Problem Domain',
        field_name='problem_domain_id',
        queryset=ProblemDomain.objects.all(),
        empty_label='Select Problem Domain',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    status = django_filters.ChoiceFilter(
        choices=STATUS,
        label='Status',
        empty_label='Select Status',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    source = django_filters.ChoiceFilter(
        choices=SOURCE,
        label='Source',
        empty_label='Select Source',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    date = django_filters.DateFilter(
        label='Date',
        field_name='issue_date',
        lookup_expr='icontains',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'datepicker',
            'type': 'text',
            'placeholder': 'YYYY - MM - DD'
        }),
    )

    class Meta:
        model = Ticket
        fields = ['client_id', 'branch_id', 'problem_domain_id', 'status', 'source', 'issue_date']



