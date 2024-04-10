from django.db import models

class Trains(models.Model):
    id = models.AutoField(primary_key=True)
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    arrets = models.IntegerField()
    h_depart = models.CharField(max_length=50)
    h_arrivee = models.CharField(max_length=50)
