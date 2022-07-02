from django.db import models

class Reactions(models.Model):
    label = models.CharField(max_length=20)
    image_url = models.CharField(max_length=20)
    