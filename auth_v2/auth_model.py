from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from models.managers.sp_managers import StoredProcedureManager

class User(AbstractBaseUser):
    objects = StoredProcedureManager('CurviDB')

    class Meta:
        app_label = 'auth_v2'

    StaffName = models.CharField(max_length=50)
    StaffUsername = models.CharField(max_length=50)
    StaffPassword = models.CharField(max_length=100)
    
    USERNAME_FIELD = "StaffUsername"