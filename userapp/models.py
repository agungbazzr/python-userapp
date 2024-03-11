import uuid
from django.db import models

class Roles(models.Model):
    roles_id = models.IntegerField(default=0)
    access_level = models.CharField(max_length=200)
    menu = models.TextField(max_length=200)


class Users(models.Model):
    roles_id = models.OneToOneField(Roles, on_delete=models.CASCADE)
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)