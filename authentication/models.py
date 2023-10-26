from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Otp(models.Model):
    email =  models.CharField(max_length=500)
    otp = models.IntegerField()
    def __str__(self):
        return self.email