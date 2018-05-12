from django.db import models
from models.managers.sp_managers import StoredProcedureManager

class PreprocessedDocument(models.Model):
    objects = StoredProcedureManager('CurviDB')

    PreprocessedID = models.BigIntegerField(primary_key=True)
    DocumentID = models.BigIntegerField()
    Token = models.TextField()
    Stemmed = models.TextField()