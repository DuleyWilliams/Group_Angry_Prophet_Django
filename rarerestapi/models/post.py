from django.db import models

from rarerestapi.models.user import User
from rarerestapi.models.categories import Categories


class Post(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    publication_date = models.DateField()
    image_url = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=20)
    approved = models.BooleanField()
