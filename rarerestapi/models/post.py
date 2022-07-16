from django.db import models

from rarerestapi.models.rare_users import RareUser
from rarerestapi.models.categories import Categories


class Post(models.Model):
    # search about relative names
    user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    publication_date = models.DateField()
    image_url = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=20)
    approved = models.BooleanField()
