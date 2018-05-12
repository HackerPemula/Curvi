from django.db import models
from models.managers.sp_managers import StoredProcedureManager

class Document(models.Model):
    objects = StoredProcedureManager('CurviDB')

    DocumentID = models.BigIntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    RegistrantID = models.CharField(max_length=20)
    DocumentUrl = models.CharField(max_length=200)
    StatusRecord = models.CharField(max_length=1)