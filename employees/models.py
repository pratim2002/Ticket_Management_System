from django.db import models

# Create your models here.
class Employee(models.Model):
    class Meta:
        ordering = ['first_name']
    first_name  = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, null=True, blank=True)
    last_name   = models.CharField(max_length=254, null=True, blank=True)
    mobile      = models.CharField(max_length=254, null=True, blank=True)
    email       = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    department  = models.CharField(max_length=254, null=True, blank=True)
    position    = models.CharField(max_length=254, null=True, blank=True)
    picture     = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.first_name