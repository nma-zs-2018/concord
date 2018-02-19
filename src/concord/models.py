from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    salt = models.TextField()
    key_public = models.TextField()
    key_private_crypted = models.TextField()

class Group(models.Model):
    group_name = models.TextField()

class UserGroupInfo(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key_symmetric_crypted = models.TextField()

