import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def uploaded(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    name = models.CharField(max_length=100)
    size = models.PositiveBigIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_upload = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=uploaded, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quality = models.CharField(max_length=100)

    class Meta:
        abstract = True



class Photo(Media):
    content = models.ImageField(upload_to=uploaded, null=True, blank=True)


class Video(Media):
    length = models.PositiveBigIntegerField()
    content = models.FileField(upload_to=uploaded, null=True, blank=True)
    preview = models.FileField(upload_to=uploaded, blank=True, null=True)
