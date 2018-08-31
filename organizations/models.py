from django.db import models

# Create your models here.
IS_ACTIVE = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )


class Organization(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    contact_person1 = models.CharField(max_length=254, null=True, blank=True)
    contact_person2 = models.CharField(max_length=254, null=True, blank=True)
    contact_person3 = models.CharField(max_length=24, null=True, blank=True)
    mobile1 = models.CharField(max_length=254, null=True, blank=True)
    mobile2 = models.CharField(max_length=254, null=True, blank=True)
    mobile3 = models.CharField(max_length=254, null=True, blank=True)
    is_active = models.CharField(max_length=254, choices=IS_ACTIVE, default=IS_ACTIVE[0][0])
    logo = models.ImageField(upload_to='logo/', height_field=None, width_field=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #Object created DateTime
    updated_at = models.DateTimeField(auto_now=True) #last modified DateTime

    def __str__(self):
        return self.name

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url