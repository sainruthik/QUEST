from django.db import models

class Train(models.Model):
    no = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    days = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    arrival = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    def __str__(self):
        return self.name
