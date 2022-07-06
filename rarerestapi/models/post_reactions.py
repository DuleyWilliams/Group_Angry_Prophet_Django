from django.db import models

from rarerestapi.models.rare_users import RareUser
from rarerestapi.models.post import Post
from rarerestapi.models.reactions import Reaction


class PostReaction(models.Model):
    """Post Reaction Model"""
    user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE)