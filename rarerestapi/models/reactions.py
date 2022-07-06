from django.db import models

class Reaction(models.Model):
    """Reaction Model"""
    label = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)