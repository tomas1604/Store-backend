from django.db import models
from .user import User

class Account (models.Model): # id, balance, lastChangeDate, isActive, user FK
    id = models.AutoField(primary_key=True)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateField()
    isActive = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
