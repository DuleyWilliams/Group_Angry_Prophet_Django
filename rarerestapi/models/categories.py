"""import statements"""
from django.db import models

class Categories(models.Model):
    """Categories model"""
    label = models.CharField(max_length=100)
