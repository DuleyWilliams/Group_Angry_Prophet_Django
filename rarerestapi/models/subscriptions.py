from django.db import models

from rarerestapi.models.rare_users import RareUser


class Subscription(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    follower_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="follower_id")
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="author_id")
    content = models.CharField(max_length=55)
    created_on = models.DateField()
    ended_on = models.DateField()
