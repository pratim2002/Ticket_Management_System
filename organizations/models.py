from django.db import models

# Create your models here.
IS_ACTIVE = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )


class Organization(models.Model):
    class Meta:
        ordering = ['name']
    username = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    mobile = models.CharField(max_length=254, null=True, blank=True)
    is_active = models.CharField(max_length=254, choices=IS_ACTIVE, default=IS_ACTIVE[0][0])
    created_at = models.DateTimeField(auto_now_add=True) #Object created DateTime
    updated_at = models.DateTimeField(auto_now=True) #last modified DateTime

    def __str__(self):
        return self.username

