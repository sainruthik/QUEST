from django.db import models
'''
category
1 -> historical
2 -> temple
3 -> beaches
4 -> parks
'''
class TouristPlaces(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    imageurl = models.CharField(max_length=200)
    category = models.IntegerField()
    def __str__(self):
        return self.name
