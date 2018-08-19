from django.db import models

from organizations.models import Organization
from employees.models import Employee
# Create your models here.
TICKET_TYPE = (
        ('PROBLEM', 'Problem'),
        ('FEATURE REQUIRED', 'Feature Required'),
        ('SUGGESTION', 'Suggestion'),
        ('OFFICIAL', 'Official'),
    )
STATUS = (
    ('OPEN', 'Open'),
    ('CLOSE', 'Close'),
    ('PENDING', 'Pending'),
)
class Ticket(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    ticket_type     = models.CharField(max_length=40, choices=TICKET_TYPE)
    description     = models.TextField(max_length=400)
    issue_date      = models.DateField(auto_now_add=True, auto_now=False)
    completion_date = models.DateField(auto_now_add=False, auto_now=False)
    status          = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])
    employee_id     = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    attached_file   = models.ImageField(upload_to='ticket_file/', null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.organization_id.name

    @property
    def attached_file_url(self):
        if self.attached_file and hasattr(self.attached_file, 'url'):
            return self.attached_file.url