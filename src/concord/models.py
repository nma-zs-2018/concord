from django.db import models
from django.contrib.auth.models import AbstractUser

class ConcordUser(AbstractUser):
    public_key = models.TextField()

class ChatGroup(models.Model):
    def __str__(self):
        return self.groupName

    groupName = models.TextField()

class ChatCryptoInfo(models.Model):
    def __str__(self):
        return str(self.chatGroup)

    chatGroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    concordUser = models.ForeignKey(ConcordUser, on_delete=models.CASCADE)
    encrypted_symetric_key = models.TextField()

