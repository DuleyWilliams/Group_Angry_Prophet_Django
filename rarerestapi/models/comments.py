from django.db import models

from rarerestapi.models.rare_users import RareUser
from rarerestapi.models.post import Post


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=55)
    created_on = models.DateTimeField()
