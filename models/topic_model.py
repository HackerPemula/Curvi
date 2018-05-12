from django.db import models
from models.managers.sp_managers import StoredProcedureManager

class Topic(models.Model):
    objects = StoredProcedureManager('CurviDB')

    TopicID = models.BigIntegerField(primary_key=True)
    EnglishTopic = models.CharField(max_length=200)
    IndonesianTopic = models.CharField(max_length=200)