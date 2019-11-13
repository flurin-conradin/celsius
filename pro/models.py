from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=200, verbose_name='station_name', unique=True)
    lon = models.IntegerField()
    lat = models.IntegerField()


class Weather(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    precipitation = models.FloatField('precipitation', null=True, blank=True) 
    temperature = models.FloatField('precipitation', null=True, blank=True)
