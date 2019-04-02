from django.db import models
from model_utils import Choices
from employees.models import Employee

# Create your models here.
SOURCE = Choices(
        'Call_in',
        'Call_out',
        'CUG',
        'Viber',
        'Skype',
        'Message',
    )
STATUS = Choices(
    'Open',
    'Close',
    'Pending',
)


class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProblemDomain(models.Model):
    problem = models.CharField(max_length=255)

    def __str__(self):
        return self.problem


class Ticket(models.Model):
    issue_date = models.DateField(auto_now_add=True, auto_now=False)
    client_id = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True, blank=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    problem_domain_id = models.ForeignKey(ProblemDomain, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS.Open)
    remarks = models.CharField(max_length=255, null=True)
    ticket = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=10, choices=SOURCE, default=SOURCE.Call_in)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_id

    @property
    def attached_file_url(self):
        if self.attached_file and hasattr(self.attached_file, 'url'):
            return self.attached_file.url


