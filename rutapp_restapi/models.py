from django.db import models

class Walk(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    region = models.CharField(max_length=100)
    length = models.DecimalField(decimal_places=2, max_digits=5)
    travel_info = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    walk_options = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    lunch_tea = models.TextField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    source_text = models.CharField(blank=True, null=True, max_length=100)
