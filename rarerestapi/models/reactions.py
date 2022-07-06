from django.db import models

class Reaction(models.Model):
    """Reaction Model"""
    label = models.CharField
    image_url = models.CharField