import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
