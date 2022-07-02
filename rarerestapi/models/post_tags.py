from django.db import models

from rarerestapi.models.post import Post
from rarerestapi.models.tag import Tag


class PostTag(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
