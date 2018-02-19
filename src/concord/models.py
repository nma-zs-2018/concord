from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    salt = models.TextField()
    key_public = models.TextField()
    key_private_crypted = models.TextField()

class Group(models.Model):
    def __str__(self):
        return self.group_name

    group_name = models.TextField()

class UserGroupInfo(models.Model):
    def __str__(self):
        return str(self.group)

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key_symmetric_crypted = models.TextField()

