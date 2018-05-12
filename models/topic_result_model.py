from django.db import models
from models.managers.sp_managers import StoredProcedureManager

class TopicResult(models.Model):
    objects = StoredProcedureManager('CurviDB')

    TopicResultID = models.BigIntegerField(primary_key=True)
    Topic = models.CharField(max_length=200)