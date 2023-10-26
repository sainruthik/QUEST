from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=30)
    categories = models.CharField(max_length=30)
    def __str__(self):
        return self.name
