
from django.db import models

from rarerestapi.models.rare_users import RareUser

class DemotionQue(models.Model):
    action = models.CharField
    admin_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    approver_one_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)