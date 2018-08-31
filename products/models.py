from django.db import models

# Create your models here.


class Product(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
