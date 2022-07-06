
from django.db import models

from rarerestapi.models.rare_users import RareUser

class DemotionQue(models.Model):
    action = models.CharField(max_length=100)
    admin_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="admin_id")
    approver_one_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="approver_one_id")