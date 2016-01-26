from django.db import models

class Walk(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    region = models.CharField(max_length=100)
    length = models.DecimalField(decimal_places=2, max_digits=5)
    travel_info = models.TextField()
