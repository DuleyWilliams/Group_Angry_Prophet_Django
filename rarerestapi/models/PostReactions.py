import imp
from django.db import models
from .rare_users import RareUser
from .post import Post
from .Reactions import Reactions

class PostReactions(models.Model):
    user_id = models.ForeignKey(RareUser,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    reaction_id = models.ForeignKey(Reactions,on_delete=models.CASCADE)